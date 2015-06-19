#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from storage.schema.deserialize import SchemaDeserializer
from models.data_types import PrimitiveDataType, ComplexDataType

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

    with open('./usage.json') as f:
        methods_usage = json.load(f)
        for m in methods_usage:
            print(m)
