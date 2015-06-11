from docx.table import Table
from docx.text.paragraph import Paragraph


def print_children(indent, node):
    for ch in node.children:
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


def print_block_type_count(n):
    table_count = 0
    paragraph_count = 0
    for b in n.blocks:
        if isinstance(b, Paragraph):
            paragraph_count += 1
        if isinstance(b, Table):
            table_count += 1
    print n.name, table_count, paragraph_count
