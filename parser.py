#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.reg import Registry
from storage.doc.decode import populate_types_from_node, populate_nodes_from_doc, populate_resources_from_node
from storage.schema.serialize import SchemaSerializer
import docx
import sys


if __name__ == '__main__':
    doc = docx.Document(sys.argv[1])
    type_reg = Registry()
    resource_reg = Registry()

    root = populate_nodes_from_doc(doc)
    populate_types_from_node(root, type_reg)
    populate_resources_from_node(root, resource_reg)

    serializer = SchemaSerializer('./schema')

    for type_name in type_reg.types:
        serializer.serialize(type_reg.get_type(type_name))

    for resource_name in resource_reg.types:
        serializer.serialize(resource_reg.get_type(resource_name))
        #res = resource_reg.get_type(resource_name)
        #for method_name in res.methods:
        #    method = res.methods[method_name]
        #    print method.name
        #    for perm_name in method.permissions:
        #        perm = method.permissions[perm_name]
        #        print ' ', perm.role, perm.access, perm.description
