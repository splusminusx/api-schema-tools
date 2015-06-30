import json
import os
from models.data_types import PrimitiveDataType, ComplexDataType
from models.resource import Resource
from models.method import Method
from models.permissions import Permission
from models.field import Field


class SchemaDeserializer(object):
    def __init__(self, path):
        self._path = path

    def decode_type(self, type_name):
        with open(os.path.join(self._path, u'Types', type_name + u'.json')) as f:
            data = json.load(f)
            if data[u'kind'] == u'ComplexDataType':
                return self._decode_complex_data_type(data)
            if data[u'kind'] == u'PrimitiveDataType':
                return self._decode_primitive_data_type(data)

    @staticmethod
    def _decode_primitive_data_type(data):
        return PrimitiveDataType(
            data[u'name'],
            data[u'description'],
            data[u'is_deprecated']
        )

    @classmethod
    def _decode_complex_data_type(cls, data):
        cdt = ComplexDataType(
            data[u'name'],
            data[u'description'],
            data[u'is_deprecated']
        )
        cls._decode_fields(data[u'fields'], cdt)
        return cdt

    @classmethod
    def _decode_type_string(cls, data):
        if data:
            if data[u'kind'] == u'Reference':
                return data[u'name']
            if data[u'kind'] == u'Generic':
                return data[u'name'] + u'.<' + cls._decode_type_string(data[u'type_parameter']) + u'>'

    def decode_resource(self, type_name):
        with open(os.path.join(self._path, u'Resources', type_name + u'.json')) as f:
            data = json.load(f)
            if data[u'kind'] == u'Resource':
                res = Resource(data[u'name'], data[u'description'])
                for method in data[u'methods']:
                    res.add_method(self._decode_method(method))
                return res

    def types(self):
        return map(
            lambda x: x.replace(u'.json', u''),
            os.listdir(os.path.join(self._path, u'Types'))
        )

    def resources(self):
        return map(
            lambda x: x.replace(u'.json', u''),
            os.listdir(os.path.join(self._path, u'Resources'))
        )

    @classmethod
    def _decode_fields(cls, data, entity):
        for field in data:
            data_type = cls._decode_type_string(field[u'type'])
            entity.add_field(
                Field(
                    field[u'name'],
                    data_type,
                    field[u'description'],
                    field[u'required']
                )
            )

    @classmethod
    def _decode_permission(cls, data):
        return Permission(
            data[u'role'],
            data[u'access'],
            data[u'description']
        )

    @classmethod
    def _decode_method(cls, data):
        met = Method(
            data[u'name'],
            data[u'description'],
            cls._decode_type_string(data[u'result_type']),
            data[u'is_deprecated']
        )

        cls._decode_fields(data[u'fields'], met)

        for perm in data[u'permissions']:
            met.add_permission(cls._decode_permission(perm))
        return met
