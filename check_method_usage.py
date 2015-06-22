#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from storage.schema.deserialize import SchemaDeserializer
from models.data_types import PrimitiveDataType, ComplexDataType


def get_full_methods_names(resources, filter=None):
    specified_methods = []
    for resource in resources:
        for method_name in resource.methods:
            if filter:
                if not filter(resource.methods[method_name]):
                    continue
            specified_methods.append(
                (resource.name + '.' + method_name).lower()
            )
    return specified_methods


def find_unused_methods(resources, used_methods):
    specified_methods = get_full_methods_names(resources)
    return set(specified_methods).difference(set(used_methods))


def find_unspecified_methods(resources, used_methods):
    specified_methods = get_full_methods_names(resources)
    return set(used_methods).difference(set(specified_methods))


def find_usage_of_deprecated_methods(resources, used_methods):
    deprecated_methods = get_full_methods_names(resources, lambda x: x.deprecated)
    return set(deprecated_methods).intersection(set(used_methods))


if __name__ == '__main__':
    deserializer = SchemaDeserializer('./schema')
    primitive_types = []
    complex_types = []
    resources = []

    data_types = deserializer.types()
    data_types.sort()
    resource_names = deserializer.resources()
    resource_names.sort()

    for type_name in data_types:
        data_type = deserializer.decode_type(type_name)
        if isinstance(data_type, ComplexDataType):
            complex_types.append(data_type)
        elif isinstance(data_type, PrimitiveDataType):
            primitive_types.append(data_type)

    for resource_name in resource_names:
        resources.append(deserializer.decode_resource(resource_name))

    with open('./schema/operation/usage.json') as f:
        data = json.load(f)
        methods_usage = []
        for m in data:
            methods_usage.append(m.lower())

        print ">>>> Unused methods"
        for unused in find_unused_methods(resources, methods_usage):
            print unused

        print "\n>>>> Unspecified methods"
        for unspecified in find_unspecified_methods(resources, methods_usage):
            print unspecified

        print "\n>>>> Deprecation usage"
        for deprecated in find_usage_of_deprecated_methods(resources, methods_usage):
            print deprecated
