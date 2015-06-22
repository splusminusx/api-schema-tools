#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storage.schema.deserialize import SchemaDeserializer
from models.data_types import ComplexDataType
from models.reg import Registry


def get_reference_type_name(field):
    name = field.datatypename
    if name:
        start_idx = name.find(u'.<')
        end_idx = name.find(u'>')
        if start_idx != -1 and end_idx != -1:
            return name[start_idx+2:end_idx]
        else:
            return name
    else:
        raise ValueError("Filed has not datatypename")


def check_field(field, type_reg, full_path):
    if field is not None:
        try:
            ref = get_reference_type_name(field)
            if ref not in type_reg.types:
                print "Unresolved reference '" + ref + "' " + full_path
        except ValueError:
            print "Unspecified data type for field " + full_path
    else:
        print "None field " + full_path


def check_complex_types(type_reg):
    for type_name in type_reg.types:
        data_type = type_reg.get_type(type_name)
        if isinstance(data_type, ComplexDataType):
            for field_name in data_type.fields:
                field = data_type.get_field(field_name)
                check_field(field, type_reg, type_name + "." + field_name)


def check_resources(resources_reg, type_reg):
    for resource_name in resources_reg.types:
        resource = resources_reg.get_type(resource_name)
        for method_name in resource.methods:
            method = resource.get_method(method_name)
            for field_name in method.fields:
                field = method.get_field(field_name)
                check_field(field, type_reg, resource_name + "." + method_name + '.' + field_name)


if __name__ == '__main__':
    deserializer = SchemaDeserializer('./schema')
    type_reg = Registry()
    resource_reg = Registry()

    data_type_names = deserializer.types()
    resource_names = deserializer.resources()

    for type_name in data_type_names:
        type_reg.add_type(deserializer.decode_type(type_name))

    for resource_name in resource_names:
        resource_reg.add_type(deserializer.decode_resource(resource_name))

    print "Complex Types Reference Errors:"
    check_complex_types(type_reg)

    print "\nResources Reference Errors:"
    check_resources(resource_reg, type_reg)
