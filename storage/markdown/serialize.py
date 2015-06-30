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

    DEPRECATION_WARNING = u'\n## WARNING: DEPRECATED\n'
    TYPE_DESCRIPTION_HEADING = u'\n### Описание типа\n'
    RESOURCE_DESCRIPTION_HEADING = u'\n## Описание ресурса\n'
    METHOD_DESCRIPTION_HEADING = u'\n### Описание метода\n'
    METHODS_HEADING = u'\n# Методы\n'
    PERMISSIONS_HEADING = u'\n### Доступы к методу\n'
    RESULT_HEADING = u'\n### Результат\n'
    FIELDS_HEADING = u'\n### Поля\n'
    FIELDS_TABLE_HEADING = u'\n| Имя поля | Необходимость | Тип данных | Комментарий |\n|---|---|---|---|\n'
    PERMISSIONS_TABLE_HEADING = u'\n| Имя роли | доступ | Комментарий |\n|---|---|---|\n'

    @staticmethod
    def escape_description(description):
        return description.replace(u'\n', '<br/>').replace(u'|', u'\|')

    def get_path(self, obj):
        if isinstance(obj, ComplexDataType) or isinstance(obj, PrimitiveDataType):
            return os.path.join(self._doc_path, 'Types', obj.name + '.md')
        if isinstance(obj, Resource):
            return os.path.join(self._doc_path, 'Resources', obj.name + '.md')

    def get_full_path(self, obj):
        return os.path.join(self._repo_path, self.get_path(obj))

    def serialize(self, obj):
        if isinstance(obj, ComplexDataType):
            self._serialize_complex_data_type(obj)
        elif isinstance(obj, PrimitiveDataType):
            self._serialize_primitive_data_type(obj)
        elif isinstance(obj, Resource):
            self._serialize_resource(obj)

    @staticmethod
    def get_data_type_link(data_type_name):
        if data_type_name:
            start_idx = data_type_name.find('.<')
            end_idx = data_type_name.find('>')
            if start_idx != -1 and end_idx != -1:
                generic_name = data_type_name[0:start_idx]
                parameter_name = data_type_name[start_idx+2:end_idx]
                return unicode(
                    generic_name +
                    u'.<[' + parameter_name + u'](' +
                    os.path.join(u'/Types', parameter_name + u')>'))
            else:
                return u'[' + data_type_name + u'](' + \
                       os.path.join(u'/Types', data_type_name + u')')
        return u'None'

    def _serialize_complex_data_type(self, obj):
        with io.open(self.get_full_path(obj), 'w', encoding='utf-8') as f:
            f.write(u'\n## ' + obj.name)
            if obj.deprecated:
                f.write(self.DEPRECATION_WARNING)
            else:
                f.write(u'\n')
            f.write(self.TYPE_DESCRIPTION_HEADING)
            f.write(self.escape_description(obj.description))
            f.write(self.FIELDS_HEADING)
            f.write(self.FIELDS_TABLE_HEADING)
            for field_name in obj.fields:
                field = obj.fields[field_name]
                f.write(
                    u'|*' + field.name +
                    u'*|' + unicode(field.required) +
                    u'|' + self.get_data_type_link(field.datatypename) +
                    u'|' + self.escape_description(field.description) +
                    u'|\n'
                )
            f.close()

    def _serialize_primitive_data_type(self, obj):
        with io.open(self.get_full_path(obj), 'w', encoding='utf-8') as f:
            f.write(u'\n## ' + obj.name)
            if obj.deprecated:
                f.write(self.DEPRECATION_WARNING)
            else:
                f.write(u'\n')
            f.write(self.TYPE_DESCRIPTION_HEADING)
            f.write(self.escape_description(obj.description))
        f.close()

    def _serialize_resource(self, obj):
        with io.open(self.get_full_path(obj), 'w', encoding='utf-8') as f:
            f.write(u'\n# ' + obj.name + u'\n')
            f.write(self.RESOURCE_DESCRIPTION_HEADING)
            f.write(self.escape_description(obj.description))
            f.write(self.METHODS_HEADING)
            for method_name in obj.methods:
                method = obj.methods[method_name]
                if method.deprecated:
                    f.write(self.DEPRECATION_WARNING)
                f.write(u'\n## ' + method.name)
                if method.deprecated:
                    f.write(self.DEPRECATION_WARNING)
                else:
                    f.write(u'\n')
                f.write(self.METHOD_DESCRIPTION_HEADING)
                f.write(self.escape_description(method.description))
                f.write(self.FIELDS_HEADING)
                f.write(self.FIELDS_TABLE_HEADING)
                for field_name in method.fields:
                    field = method.fields[field_name]
                    f.write(
                        u'|*' + field.name +
                        u'*|' + unicode(field.required) +
                        u'|' + self.get_data_type_link(field.datatypename) +
                        u'|' + self.escape_description(field.description) +
                        u'|\n'
                    )

                f.write(self.RESULT_HEADING)
                f.write(self.get_data_type_link(method.result_type_name))

                f.write(self.PERMISSIONS_HEADING)
                f.write(self.PERMISSIONS_TABLE_HEADING)
                for perm_name in method.permissions:
                    perm = method.permissions[perm_name]
                    f.write(
                        u'|*' + unicode(perm.role) +
                        u'*|' + unicode(perm.access) +
                        u'|' + unicode(self.escape_description(perm.description)) +
                        u'|\n'
                    )

            f.close()


class MarkdownImplSerializer(object):
    METHODS_HEADING = u'## Методы\n'
    METHOD_DESCRIPTION = u'\n## Описание методы:\n'
    METHOD_RESULT = u'\n## Результат:\n'
    METHOD_IMPLEMENTATION = u'\n## Параметры реализации:\n' + \
                            u'| Атрибут | Значение |\n|---|---|\n'
    PUBLIC_FIELDS_HEADING = u'\n## Публичные поля:\n'
    PRIVATE_FIELDS_HEADING = u'\n## Приватные поля:\n'
    QUERY_FIELD = u'\n## Поля выборки:\n'
    PERMISSIONS_HEADING = u'\n## Доступы к методу\n'

    def __init__(self, repo_path, doc_path):
        self._repo_path = repo_path
        self._doc_path = doc_path
        self._serializer = MarkdownSerializer(self._repo_path, self._doc_path)

    @staticmethod
    def _get_method_link(resource, method):
        resource_path = os.path.join(u'/Resources', resource.name)
        return u'[' + method.name + u'](' + os.path.join(resource_path, method.name) + u')'

    def _serialize_resource(self, resource):
        resource_path = self._serializer.get_full_path(resource)
        with io.open(resource_path, u'w', encoding='utf-8') as f:
            f.write(u'# Ресурс: ' + resource.name + u'\n')
            f.write(MarkdownSerializer.RESOURCE_DESCRIPTION_HEADING)
            f.write(self._serializer.escape_description(resource.description))
            f.write(self.METHODS_HEADING)
            for method_name in sorted(resource.methods.keys()):
                method = resource.get_method(method_name)
                f.write(u'- ' + self._get_method_link(resource, method) + u'\n')

    def _serialize_method(self, resource, method):
        resource_path = self._serializer.get_full_path(resource)
        resource_dir = resource_path[0:-3]
        with io.open(os.path.join(resource_dir, method.name + u'.md'), u'w', encoding='utf-8') as f:
            if method.is_private:
                f.write(u'# Приватный метод: ')
            else:
                f.write(u'# Публичный метод: ')
            f.write(resource.name + u'.' + method.name)
            if method.deprecated:
                f.write(MarkdownSerializer.DEPRECATION_WARNING)
            else:
                f.write(u'\n')
            f.write(self.METHOD_DESCRIPTION)
            f.write(self._serializer.escape_description(method.description) + u'\n')
            f.write(self.METHOD_RESULT)
            f.write(MarkdownSerializer.get_data_type_link(method.result_type_name) + u'\n')
            f.write(self.METHOD_IMPLEMENTATION)
            f.write(u'|*Необходима аутентификация*|' + unicode(method.auth_required) + u'|\n')
            f.write(u'|*Частота запросов*|' + unicode(method.frequency) + u'|\n')
            f.write(u'|*Ограничение на количество запросов*|' + unicode(method.request_limit) + u'|\n')
            f.write(u'|*Ограничение по времени*|' + unicode(method.time_limit) + u'|\n')
            f.write(self.PUBLIC_FIELDS_HEADING)
            f.write(MarkdownSerializer.FIELDS_TABLE_HEADING)
            for field_name in method.fields:
                field = method.get_field(field_name)
                f.write(
                    u'|*' + field.name +
                    u'*|' + unicode(field.required) +
                    u'|' + MarkdownSerializer.get_data_type_link(field.datatypename) +
                    u'|' + MarkdownSerializer.escape_description(field.description) +
                    u'|\n'
                )
            f.write(self.PRIVATE_FIELDS_HEADING)
            f.write(MarkdownSerializer.FIELDS_TABLE_HEADING)
            for field_name in method.private_fields():
                field = method.get_private_field(field_name)
                f.write(
                    u'|*' + field.name +
                    u'*|' + unicode(field.required) +
                    u'|' + MarkdownSerializer.get_data_type_link(field.datatypename) +
                    u'|' + MarkdownSerializer.escape_description(field.description) +
                    u'|\n'
                )
            f.write(self.QUERY_FIELD)
            for query_name in method.get_query_names():
                f.write(u'### Запрос: ' + query_name)
                f.write(MarkdownSerializer.FIELDS_TABLE_HEADING)
                for field in method.get_query_fields(query_name):
                    f.write(
                        u'|*' + field.name +
                        u'*|' + unicode(field.required) +
                        u'|' + MarkdownSerializer.get_data_type_link(field.datatypename) +
                        u'|' + MarkdownSerializer.escape_description(field.description) +
                        u'|\n'
                    )
            f.write(self.PERMISSIONS_HEADING)
            f.write(MarkdownSerializer.PERMISSIONS_TABLE_HEADING)
            for perm_name in method.permissions:
                perm = method.permissions[perm_name]
                f.write(
                    u'|*' + unicode(perm.role) +
                    u'*|' + unicode(perm.access) +
                    u'|' + unicode(MarkdownSerializer.escape_description(unicode(perm.description))) +
                    u'|\n'
                )

    def serialize_resource(self, resource):
        resource_path = self._serializer.get_full_path(resource)
        resource_dir = resource_path[0:-3]
        if not os.path.exists(resource_dir):
            os.makedirs(resource_dir)
        self._serialize_resource(resource)
        for method_name in resource.methods:
            method = resource.get_method(method_name)
            self._serialize_method(resource, method)
