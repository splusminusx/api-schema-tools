#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import docx


def iter_block_items(parent):
    """
    Yield each paragraph and table child within *parent*, in document order.
    Each returned value is an instance of either Table or Paragraph. *parent*
    would most commonly be a reference to a main Document object, but
    also works for a _Cell object, which itself can contain paragraphs and tables.
    """
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

class Node:
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

if __name__ == '__main__':
    doc = docx.Document('apiv2.docx')

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

    names = map(lambda x: x.name, root._children[1]._children[1]._children)
    for n in names:
        print n

