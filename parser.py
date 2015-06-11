#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.data_types import ComplexDataType
from models.reg import Registry
from storage.doc.decode import populate_types_from_node, populate_nodes_from_doc, populate_resources_from_node
import docx
import sys


if __name__ == '__main__':
    doc = docx.Document(sys.argv[1])
    type_reg = Registry()
    resource_reg = Registry()

    root = populate_nodes_from_doc(doc)
    populate_types_from_node(root, type_reg)
    populate_resources_from_node(root, resource_reg)

    for type_name in type_reg.types:
        data_type = type_reg.types[type_name]
        #print data_type.name, data_type.deprecated
        if isinstance(data_type, ComplexDataType):
            for field_name in data_type.fields:
                field = data_type.get_field(field_name)
                #print ' ', field.name, field.datatypename, field.required
