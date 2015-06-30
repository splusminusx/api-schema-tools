from models.data_types import ComplexDataType, PrimitiveDataType
from models.resource import Resource
from models.field import Field
import io
import os
import json


class SchemaSerializer(object):
    def __init__(self, path):
        self._path = path

    def get_path(self, obj):
        if isinstance(obj, ComplexDataType) or isinstance(obj, PrimitiveDataType):
            return os.path.join(self._path, u'Types', obj.name + '.json')
        if isinstance(obj, Resource):
            return os.path.join(self._path, u'Resources', obj.name + '.json')

    def serialize(self, obj):
        with io.open(self.get_path(obj), 'w', encoding='utf-8') as f:
            data = None
            if isinstance(obj, ComplexDataType):
                data = self._serialize_complex_type(obj)
            elif isinstance(obj, PrimitiveDataType):
                data = self._serialize_primitive_type(obj)
            elif isinstance(obj, Resource):
                data = self._serialize_resource(obj)
            f.write(unicode(json.dumps(data, ensure_ascii=False, indent=4)))

    def _serialize_complex_type(self, obj):
        data = dict()
        data[u'kind'] = u'ComplexDataType'
        data[u'name'] = obj.name
        data[u'description'] = obj.description
        data[u'is_deprecated'] = obj.deprecated
        data[u'fields'] = []

        for field in obj.fields:
            data[u'fields'].append(self._serialize_field(obj.fields[field]))

        return data

    def _serialize_method(self, obj):
        data = dict()
        data[u'kind'] = u'Method'
        data[u'name'] = obj.name
        data[u'description'] = obj.description
        data[u'is_deprecated'] = obj.deprecated
        data[u'result_type'] = self._serialize_type(obj.result_type_name)
        data[u'permissions'] = []
        data[u'fields'] = []

        for field in obj.fields:
            data[u'fields'].append(self._serialize_field(obj.fields[field]))

        for perm in obj.permissions:
            data[u'permissions'].append(self._serialize_permission(obj.permissions[perm]))

        return data

    @staticmethod
    def _serialize_permission(obj):
        data = dict()
        data[u'kind'] = u'Permission'
        data[u'role'] = obj.role
        data[u'access'] = obj.access
        data[u'description'] = obj.description

        return data

    def _serialize_resource(self, obj):
        data = dict()
        data[u'kind'] = u'Resource'
        data[u'name'] = obj.name
        data[u'description'] = obj.description
        data[u'methods'] = []

        for method in obj.methods:
            data[u'methods'].append(self._serialize_method(obj.methods[method]))

        return data

    @staticmethod
    def _serialize_primitive_type(obj):
        data = dict()
        data[u'kind'] = u'PrimitiveDataType'
        data[u'name'] = obj.name
        data[u'description'] = obj.description
        data[u'is_deprecated'] = obj.deprecated

        return data

    @classmethod
    def _serialize_field(cls, field):
        if isinstance(field, Field):
            data = dict()
            data[u'kind'] = u'field'
            data[u'name'] = field.name
            data[u'type'] = cls._serialize_type(field.datatypename)
            data[u'description'] = field.description
            data[u'required'] = field.required

            return data
        else:
            TypeError('Argument must be Field.')

    @classmethod
    def _serialize_type(cls, type_string):
        if type_string:
            start_idx = type_string.find(u'.<')
            end_idx = type_string.find(u'>')
            if start_idx != -1 and end_idx != -1:
                return cls._serialize_generic(
                    type_string[0:start_idx],
                    type_string[start_idx+2:end_idx]
                )
            else:
                return cls._serialize_reference(type_string)

    @staticmethod
    def _serialize_reference(type_name):
        data = dict()
        data['kind'] = 'Reference'
        data['name'] = type_name

        return data

    @classmethod
    def _serialize_generic(cls, type_name, type_parameter):
        data = dict()
        data['kind'] = 'Generic'
        data['name'] = type_name
        data['type_parameter'] = cls._serialize_reference(type_parameter)

        return data
