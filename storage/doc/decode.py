#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docx.table import Table
from docx.text.paragraph import Paragraph
from storage.doc.helpers import join_paragraphs, iter_block_items
from storage.doc.model import Node
from models.data_types import PrimitiveDataType, ComplexDataType
from models.resource import Resource
from view.helpers import print_block_type_count


def populate_primitive_types(registry, table):
    for row in table.rows[1:]:
        name = row.cells[0].paragraphs[0].text.strip()
        description = join_paragraphs(row.cells[1].paragraphs)
        registry.add_type(PrimitiveDataType(name, description))


def populate_fields(data_type, table):
    for row in table.rows[1:]:
        name = row.cells[0].paragraphs[0].text.strip()
        datatypename = row.cells[2].paragraphs[0].text.strip()
        required = row.cells[1].paragraphs[0].text.strip() == u'+'
        description = join_paragraphs(row.cells[3].paragraphs)
        data_type.add_field(name, datatypename, description, required)


def get_complex_type_name(node):
    node_names = node.name.strip().split(u' ')
    if u'-' in node_names:
        node_names.remove(u'-')
    return node_names[0]


def is_complex_type_deprecated(node):
    node_names = node.name.strip().split(u' ')
    return u'DEPRECATED' in node_names


def get_complex_type_description(node):
    paragraphs = []
    for b in node.blocks:
        if isinstance(b, Paragraph):
            paragraphs.append(b)
    return join_paragraphs(paragraphs)


def populate_complex_type(registry, node):
    deprecated = is_complex_type_deprecated(node)
    name = get_complex_type_name(node)

    field_table = None
    for b in node.blocks:
        if isinstance(b, Table):
            field_table = b
    description = get_complex_type_description(node)

    data_type = ComplexDataType(name, description, deprecated)
    if field_table:
        populate_fields(data_type, field_table)

    registry.add_type(data_type)

    for ch in node.children:
        populate_complex_type(registry, ch)


def get_heading_level(prev_level, block):
    if is_heading(block):
        return int(block.style.name[-1])
    else:
        return prev_level


def is_heading(block):
    return (isinstance(block, Paragraph) and
            (block.style.name.startswith(u'Заголовок') or
             block.style.name.startswith(u'Heading')))


def populate_nodes_from_doc(doc):
    root = Node(u'root')
    current_node = root
    current_level = 0

    for block in iter_block_items(doc):
        if is_heading(block):
            level = get_heading_level(current_level, block)
            if current_level >= level:
                for _ in range(0, current_level - level + 1):
                    current_node = current_node.parent
            node = Node(block.text, current_node)
            current_node = node
            current_level = level
        current_node.add_block(block)

    return root


def populate_types_from_node(root, reg):
    # Populate Primitive Data Types
    primitive_type_blocks = root.children[1].children[0].blocks
    for block in primitive_type_blocks:
        if isinstance(block, Table):
            populate_primitive_types(reg, block)

    # Populate Complex Data Types
    complex_type_nodes = root.children[1].children[1].children
    for node in complex_type_nodes:
        populate_complex_type(reg, node)


def parse_method_name(name):
    return name.split(u'.')[1]


def populate_resource(reg, node):
    res = Resource(get_complex_type_name(node),
                   get_complex_type_description(node))

    print res.name
    print res.description

    for ch in node.children:
        method = ComplexDataType(get_complex_type_name(node),
                                 get_complex_type_description(node),
                                 is_complex_type_deprecated(node))


        #print_block_type_count(ch)
        #print get_complex_type_name(ch)
        #print is_complex_type_deprecated(ch)
        #print parse_method_name(ch.name)

def populate_resources_from_node(root, reg):
    for node in root.children[2].children:
        populate_resource(reg, node)
