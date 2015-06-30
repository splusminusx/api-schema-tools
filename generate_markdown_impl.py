#!/usr/bin/env python
# -*- coding: utf-8 -*-
from storage.impl.deserialize import Deserializer
from storage.schema.deserialize import SchemaDeserializer
from storage.markdown.serialize import MarkdownImplSerializer, MarkdownSerializer
from models.reg import Registry
from models.data_types import ComplexDataType, PrimitiveDataType
import io
import os


if __name__ == u'__main__':
    resource_decoder = Deserializer(u'./schema/merged')
    resource_registry = Registry()

    type_decoder = SchemaDeserializer(u'./schema/merged')
    type_registry = Registry()

    resource_serializer = MarkdownImplSerializer(u'.', u'docs')
    type_serializer = MarkdownSerializer(u'.', u'docs')

    for name in resource_decoder.resources():
        res = resource_decoder.decode_resource(name)
        resource_registry.add_type(res)
        resource_serializer.serialize_resource(res)

    for name in type_decoder.types():
        type = type_decoder.decode_type(name)
        type_registry.add_type(type)
        type_serializer.serialize(type)

    primitive_types = []
    complex_types = []
    for name in sorted(type_registry.types.keys()):
        type = type_registry.get_type(name)
        if isinstance(type, ComplexDataType):
            complex_types.append(type)
        elif isinstance(type, PrimitiveDataType):
            primitive_types.append(type)

    with io.open(os.path.join(u'./', u'docs', u'index.md'), u'w', encoding='utf-8') as output:
        output.write(u'# APIv2 Documentation\n')
        output.write(u'## Простые типы данных\n')
        for type in primitive_types:
            output.write(u'- [' + type.name + u'](/Types/' + type.name + u')\n')
        output.write(u'## Сложные типы данных\n')
        for type in complex_types:
            output.write(u'- [' + type.name + u'](/Types/' + type.name + u')\n')

        output.write(u'## Ресурсы\n')
        for name in sorted(resource_registry.types.keys()):
            output.write(u'- [' + name + u'](/Resources/' + name + u')\n')
