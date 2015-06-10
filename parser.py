#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import docx
import sys


def iter_block_items(parent):
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self._parent = parent
        if parent:
            parent.add_child(self)
        self._blocks = []
        self._children = []

    def add_block(self, blocki):
        self._blocks.append(block)

    def add_child(self, child):
        child._parent = self
        self._children.append(child)

    def blocks(self):
        return self._blocaks


def print_children(indent, node):
    for ch in node._children:
        print ' '*indent, ch.name
        print_children(indent+1, ch)


def print_block(block):
    if isinstance(block, Paragraph):
        print_paragraph(block)
    if isinstance(block, Table):
        print_table(block)


def print_paragraph(p):
    print p.text


def print_cell(cell):
    for p in cell.paragraphs:
        print_paragraph(p)


def print_table(t):
    for row in t.rows:
        for cell in row.cells:
            print_cell(cell)


class PrimitiveDataType(object):
    def __init__(self, name, description, deprecated=False):
        self._name = name
        self._description = description
        self._deprecated = deprecated

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def deprecated(self):
        return self._deprecated


class Field(object):
    def __init__(self, name, datatypename, description, required):
        self._name = name
        self._datatypename = datatypename
        self._description = description
        self._required = required

    @property
    def name(self):
        return self._name

    @property
    def datatypename(self):
        return self._datatypename

    @property
    def description(self):
        return self._description

    @property
    def required(self):
        return self._required


class ComplexDataType(PrimitiveDataType):
    def __init__(self, name, description, deprecated=False):
        super(ComplexDataType, self).__init__(name, description, deprecated)
        self._fields = {}

    def add_field(self, name, datatypename, description, required=False):
        self._fields[name] = Field(name, datatypename, description, required)

    def get_field(self, name):
        return self._fields[name]

    def has_field(self, name):
        return name in self._fields


class DataTypeRegistry(object):
    def __init__(self):
        self._registry = {}

    def add_type(self, datatype):
        self._registry[datatype.name] = datatype

    def get_type(self, name):
        return self._registry[name]

    def type_defined(self, name):
        return name in self._registry


def join_paragraphs(ps):
    result = ''
    for p in ps:
        result += p.text + '\n'
    return result


def populate_primitive_types(reg, table):
    for row in table.rows[1:]:
        name = row.cells[0].paragraphs[0].text.strip()
        description = join_paragraphs(row.cells[1].paragraphs)
        reg.add_type(PrimitiveDataType(name, description))


def print_block_type_count(node):
    table_count = 0
    paragraph_count = 0
    for block in node._blocks:
        if isinstance(block, Paragraph):
            paragraph_count += 1
        if isinstance(block, Table):
            table_count += 1
    #print node.name, ': tables =', table_count, 'paragraphs =', paragraph_count
    print node.name, table_count


def populate_fields(datatype, table):
    for row in table.rows[1:]:
        name = row.cells[0].paragraphs[0].text.strip()
        datatypename = row.cells[2].paragraphs[0].text.strip()
        required = row.cells[1].paragraphs[0].text.strip() == u'+'
        description = join_paragraphs(row.cells[3].paragraphs)
        datatype.add_field(name, datatypename, description, required)


def populate_complex_type(reg, node):
    deprecated = False
    nodenames = node.name.strip().split(' ')
    if '-' in nodenames:
        nodenames.remove('-')
    if 'DEPRECATED' in nodenames:
        deprecated = True
        nodenames.remove('DEPRECATED')

    name = nodenames[0]

    paragraphs = []
    field_table = None
    for block in node._blocks:
        if isinstance(block, Paragraph):
            paragraphs.append(block)
        if isinstance(block, Table):
            field_table = block
    description = join_paragraphs(paragraphs)

    datatype = ComplexDataType(name, description, deprecated)
    if field_table:
        populate_fields(datatype, field_table)

    reg.add_type(datatype)

    for ch in node._children:
        populate_complex_type(reg, ch)


if __name__ == '__main__':
    doc = docx.Document(sys.argv[1])

    root = Node('root')
    current_node = root
    current_level = 0

    for block in iter_block_items(doc):
        if isinstance(block, Paragraph) and block.style.name.startswith(u'Заголовок'):
            level = int(block.style.name[-1])
            if current_level >= level:
                for _ in range(0, current_level - level + 1):
                    current_node = current_node._parent
            node = Node(block.text, current_node)
            current_node = node
            current_level = level
        current_node.add_block(block)

    print_children(0, root)
    print ">>>>\n"

    reg = DataTypeRegistry()

    # Populate Primitive Data Types
    for block in root._children[1]._children[0]._blocks:
        if isinstance(block, Table):
            populate_primitive_types(reg, block)

    for t in reg._registry:
        print reg._registry[t].name


    # Populate Complex Data Types
    for node in root._children[1]._children[1]._children:
        populate_complex_type(reg, node)


    print "with complex types >>"
    for t in reg._registry:
        dt = reg._registry[t]
        if isinstance(dt, ComplexDataType):
            print dt.name, dt.deprecated
            for f in dt._fields:
                fd = dt.get_field(f)
                print ' ', fd.name, fd.datatypename, fd.required

