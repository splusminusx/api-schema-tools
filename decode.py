#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from storage.schema.deserialize import SchemaDeserializer
from storage.markdown.serialize import MarkdownSerializer
from models.data_types import PrimitiveDataType, ComplexDataType

if __name__ == '__main__':
    deserializer = SchemaDeserializer('./schema')
    serializer = MarkdownSerializer('./', 'docs/')
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

    with io.open(u'./docs/index.md', 'w', encoding='utf-8') as f:
        f.write(u'# Содержание\n')
        f.write(u'\n## Типы данных\n')
        f.write(u'\n### Примитивные типы данных\n')
        for primitive_type in primitive_types:
            serializer.serialize(primitive_type)
            f.write(u'- [' + primitive_type.name + u'](/types/' + primitive_type.name + u')')
            if primitive_type.deprecated:
                f.write(u' - WARNING: DEPRECATED\n')
            else:
                f.write(u'\n')
        f.write(u'\n### Комплексные типы данных\n')
        for complex_type in complex_types:
            serializer.serialize(complex_type)
            f.write(u'- [' + complex_type.name + u'](/types/' + complex_type.name + u')')
            if complex_type.deprecated:
                f.write(u' - WARNING: DEPRECATED\n')
            else:
                f.write(u'\n')
        f.write(u'\n## Ресурсы\n')
        for resource in resources:
            serializer.serialize(resource)
            f.write(u'- [' + resource.name + u'](/resources/' + resource.name + u')\n')
