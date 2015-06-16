#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.data_types import ComplexDataType, PrimitiveDataType
from models.resource import Resource
import io
import os


class MarkdownSerializer(object):
    def __init__(self, repo_path, doc_path):
        self._repo_path = repo_path
        self._doc_path = doc_path

    DEPRECATION_WARNING = u'\n## WARNING: Type is DEPRECATED\n'
    TYPE_DESCRIPTION_HEADING = u'\n### Описание типа\n'
    RESOURCE_DESCRIPTION_HEADING = u'\n## Описание ресурса\n'
    METHOD_DESCRIPTION_HEADING = u'\n### Описание метода\n'
    METHODS_HEADING = u'\n# Методы\n'
    PERMISSIONS_HEADING = u'\n### Доступы к методу\n'
    FIELDS_HEADING = u'\n### Поля\n'
    FIELDS_TABLE_HEADING = u'\n| Имя поля | Необходимость | Тип данных | Комментарий |\n|---|---|---|---|\n'
    PERMISSIONS_TABLE_HEADING = u'\n| Имя роли | доступ | Комментарий |\n|---|---|---|\n'

    @staticmethod
    def _escape_description(description):
        return description.replace(u'\n', '<br/>').replace(u'|', u'\|')

    def _get_path(self, obj):
        if isinstance(obj, ComplexDataType) or isinstance(obj, PrimitiveDataType):
            return os.path.join(self._doc_path, 'types', obj.name + '.md')
        if isinstance(obj, Resource):
            return os.path.join(self._doc_path, 'resources', obj.name + '.md')

    def _get_full_path(self, obj):
        return os.path.join(self._repo_path, self._get_path(obj))

    def serialize(self, obj):
        if isinstance(obj, ComplexDataType):
            self._serialize_complex_data_type(obj)
        elif isinstance(obj, PrimitiveDataType):
            self._serialize_primitive_data_type(obj)
        elif isinstance(obj, Resource):
            self._serialize_resource(obj)

    def _get_data_type_link(self, data_type_name):
        if data_type_name:
            start_idx = data_type_name.find('.<')
            end_idx = data_type_name.find('>')
            if start_idx != -1 and end_idx != -1:
                generic_name = data_type_name[0:start_idx]
                parameter_name = data_type_name[start_idx+2:end_idx]
                return unicode(
                    generic_name +
                    u'.<[' + parameter_name + u'](' +
                    os.path.join(u'types', parameter_name + u'.md)>'))

    def _serialize_complex_data_type(self, obj):
        with io.open(self._get_full_path(obj), 'w', encoding='utf-8') as f:
            if obj.deprecated:
                f.write(self.DEPRECATION_WARNING)
            f.write(u'\n## ' + obj.name + u'\n')
            f.write(self.TYPE_DESCRIPTION_HEADING)
            f.write(obj.description)
            f.write(self.FIELDS_HEADING)
            f.write(self.FIELDS_TABLE_HEADING)
            for field_name in obj.fields:
                field = obj.fields[field_name]
                f.write(
                    u'|' + field.name +
                    u'|' + unicode(field.required) +
                    u'|' + unicode(field.datatypename) +
                    u'|' + self._escape_description(field.description) +
                    u'|\n'
                )
            f.close()

    def _serialize_primitive_data_type(self, obj):
        with io.open(self._get_full_path(obj), 'w', encoding='utf-8') as f:
            if obj.deprecated:
                f.write(self.DEPRECATION_WARNING)
            f.write(u'\n## ' + obj.name + u'\n')
            f.write(self.TYPE_DESCRIPTION_HEADING)
            f.write(obj.description)
        f.close()

    def _serialize_resource(self, obj):
        with io.open(self._get_full_path(obj), 'w', encoding='utf-8') as f:
            f.write(u'\n# ' + obj.name + u'\n')
            f.write(self.RESOURCE_DESCRIPTION_HEADING)
            f.write(obj.description)
            f.write(self.METHODS_HEADING)
            for method_name in obj.methods:
                method = obj.methods[method_name]
                if method.deprecated:
                    f.write(self.DEPRECATION_WARNING)
                f.write(u'\n## ' + method.name + u'\n')
                f.write(self.METHOD_DESCRIPTION_HEADING)
                f.write(method.description)
                f.write(self.FIELDS_HEADING)
                f.write(self.FIELDS_TABLE_HEADING)
                for field_name in method.fields:
                    field = method.fields[field_name]
                    f.write(
                        u'|' + field.name +
                        u'|' + unicode(field.required) +
                        u'|' + unicode(field.datatypename) +
                        u'|' + self._escape_description(field.description) +
                        u'|\n'
                    )

                f.write(self.PERMISSIONS_HEADING)
                f.write(self.PERMISSIONS_TABLE_HEADING)
                for perm_name in method.permissions:
                    perm = method.permissions[perm_name]
                    f.write(
                        u'|' + unicode(perm.role) or u'' +
                        u'|' + unicode(perm.access) or u'' +
                        u'|' + unicode(perm.description) or u'' +
                        u'|\n'
                    )

            f.close()
