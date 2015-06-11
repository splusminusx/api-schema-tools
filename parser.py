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
        resource = type_reg.types[type_name]
        print resource.name, resource.deprecated
        if isinstance(resource, ComplexDataType):
            for field_name in resource.fields:
                field = resource.get_field(field_name)
                print ' ', field.name, field.datatypename, field.required

    for resource_name in resource_reg.types:
        resource = resource_reg.get_type(resource_name)
        print resource.name
        for method_name in resource.methods:
            method = resource.get_method(method_name)
            print ' ', method.name, method.deprecated, method.description
            for field_name in method.fields:
                field = method.get_field(field_name)
                print '  ', field.name, field.datatypename, field.required
