#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.reg import Registry
from storage.schema.deserialize import SchemaDeserializer
from storage.impl.merge_serializer import MergeSerializer


if __name__ == '__main__':
    deserializer = SchemaDeserializer('./schema')
    serializer = MergeSerializer('./schema/implementation', './schema/merged')
    resource_reg = Registry()

    for type_name in deserializer.resources():
        resource_reg.add_type(deserializer.decode_resource(type_name))

    for type_name in resource_reg.types:
        serializer._serialize_resource(resource_reg.get_type(type_name))
