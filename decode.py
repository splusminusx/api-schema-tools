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
        print data_type
        if isinstance(data_type, ComplexDataType):
            complex_types.append(data_type)
        elif isinstance(data_type, PrimitiveDataType):
            primitive_types.append(data_type)

    for resource_name in resource_names:
        resources.append(deserializer.decode_resource(resource_name))

    with io.open(u'./docs/README.md', 'w', encoding='utf-8') as f:
        f.write(u'# Содержание\n')
        f.write(u'## Типы данных\n')
        f.write(u'### Примитивные типы данных\n')
        for primitive_type in primitive_types:
            serializer.serialize(primitive_type)
            f.write(u'- [' + primitive_type.name + u'](docs/types/' + primitive_type.name + u'.md)\n')
        f.write(u'### Комплексные типы данных\n')
        for complex_type in complex_types:
            serializer.serialize(complex_type)
            f.write(u'- [' + complex_type.name + u'](docs/types/' + complex_type.name + u'.md)\n')
        f.write(u'## Ресурсы\n')
        for resource in resources:
            serializer.serialize(resource)
            f.write(u'- [' + complex_type.name + u'](docs/resources/' + complex_type.name + u'.md)\n')
