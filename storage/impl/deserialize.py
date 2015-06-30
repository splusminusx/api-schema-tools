#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.method import ImplMethod
from models.resource import Resource
from models.field import ValidatableField
from models.validator import *
from models.permissions import Role, Access, Permission
from storage.impl.attrs import ImplResourceAttributes
from storage.schema import deserialize
import json
import os


class ImplMethodAttributes(object):
    FIELDS = 'fields'
    FIELDS_VALIDATION = 'fields_validation'
    FREQUENCY = 'frequency'  # ограничение на количество запросов. default 10 запросов в 10 сек. ???
    NO_AUTH_REQUIRED = 'no-auth-required'  # без авторизации
    PRIVATE = 'private'  # доступен только в secureLogin точке доступа
    PRIVATE_FIELDS = 'private_fields'  # поля доступены только в secureLogin точке доступа
    REQUEST_LIMIT = 'request_limit'  # ???
    TIME_LIMIT = 'time_limit'  # ???


class Deserializer(object):
    def __init__(self, path):
        self._path = path
        self._permissions = {}
        with open(self._permissions_path()) as f:
            self._permissions = json.load(f)

    def resources(self):
        return map(
            lambda x: x.replace(u'.json', u''),
            os.listdir(os.path.join(self._path, u'Methods'))
        )

    def _permissions_path(self):
        return os.path.join(self._path, u'Roles.json')

    def _decode_permissions(self, resource, method):
        permissions = []
        for role in Role.ROLES:
            role_permissions = self._permissions[role][u'permissions']
            if resource in role_permissions:
                if (isinstance(role_permissions[resource], list) and
                        len(role_permissions[resource]) > 0 and
                        role_permissions[resource][0] == u'*'):
                    permissions.append(Permission(role, Access.FULL))
                elif method in role_permissions[resource]:
                    level = role_permissions[resource][method]['level']
                    permissions.append(Permission(role, level))
        return permissions

    @staticmethod
    def _decode_validators(fields):
        validators = []
        for field in fields:
            if field[0] == FieldConstrains.ALLOW_EMPTY:
                validators.append(EmptinessValidator(True))
            elif field[0] == FieldConstrains.NON_EMPTY:
                validators.append(EmptinessValidator(False))
            elif field[0] == FieldConstrains.REQUIRED:
                validators.append(RequiredFieldValidator.build(field))
            elif field[0] == FieldConstrains.ARRAY_OF:
                validators.append(GenericTypeValidation.build(field))
            elif field[0] == FieldConstrains.ID_LIST:
                validators.append(IdListValidation.build(field))
            elif field[0] == FieldConstrains.TYPE_OF:
                validators.append(TypeReferenceValidation.build(field))
            elif field[0] == FieldConstrains.LENGTH:
                validators.append(LengthValidation.build(field))
            elif field[0] == FieldConstrains.MATCH:
                validators.append(MatchValidator.build(field))
            elif field[0] == FieldConstrains.DIGIT:
                validators.append(DigitValidation.build(field))
            elif field[0] == FieldConstrains.INTEGER:
                validators.append(IntegerValidation.build(field))
            elif field[0] == FieldConstrains.ENUM:
                validators.append(EnumValidation.build(field))
            elif field[0] == FieldConstrains.FILE:
                validators.append(FileValidation.build(field))
            elif field[0] in FieldConstrains.PRIMITIVE_DATA_TYPES:
                validators.append(PrimitiveTypeValidation.build(field))
            elif field[0] == FieldConstrains.STRING:
                validators.append(StringValidator.build(field))
            elif field[0] == FieldConstrains.DATETIME:
                validators.append(DateTimeValidator.build(field))
            if field[0] == FieldConstrains.BOOLEAN:
                validators.append(BooleanValidator.build(field))
        return validators

    @staticmethod
    def _decode_data_type(validators):
        data_type_name = u'string'
        for val in validators:
            if isinstance(val, GenericTypeValidation):
                data_type_name = val.type + u'.<' + val.parameter.split(u'\\')[-1] + u'>'
            elif isinstance(val, IdListValidation):
                data_type_name = u'idlist'
            elif isinstance(val, TypeReferenceValidation):
                data_type_name = val.type.split(u'\\')[-1]
            elif isinstance(val, DigitValidation):
                data_type_name = u'numeric'
            elif isinstance(val, IntegerValidation):
                data_type_name = u'numeric'
            elif isinstance(val, EnumValidation):
                data_type_name = u'string'
            elif isinstance(val, FileValidation):
                data_type_name = u'file'
            elif isinstance(val, PrimitiveTypeValidation):
                data_type_name = val.type_name
            elif isinstance(val, StringValidator):
                data_type_name = u'string'
            elif isinstance(val, DateTimeValidator):
                data_type_name = u'datetime'
            elif isinstance(val, BooleanValidator):
                data_type_name = u'boolean'
        return data_type_name

    @staticmethod
    def _decode_required(validators):
        required = False
        for val in validators:
            if isinstance(val, RequiredFieldValidator):
                required = val.required
        return required

    @staticmethod
    def _decode_default(validators):
        default = None
        for val in validators:
            if isinstance(val, RequiredFieldValidator):
                default = val.default
        return default

    @staticmethod
    def _decode_field(name, fields, description):
        field_validators = Deserializer._decode_validators(fields)

        data_type_name = Deserializer._decode_data_type(field_validators)
        required = Deserializer._decode_required(field_validators)
        default = Deserializer._decode_default(field_validators)

        field = ValidatableField(name, data_type_name, description, required, default)
        for val in field_validators:
            field.add_validator(val)

        return field

    def decode_resource(self, name):
        resource = Resource(name, u'')
        with open(os.path.join(self._path, u'Methods', name + u'.json')) as f:
            data = json.load(f)

            for method_name in data:
                method_data = data[method_name]
                fields = method_data.get(ImplMethodAttributes.FIELDS, {})
                fields_validation = method_data.get(
                    ImplMethodAttributes.FIELDS_VALIDATION, {})
                private_fields = method_data.get(
                    ImplMethodAttributes.PRIVATE_FIELDS, {})
                fields_descriptions = method_data.get(ImplResourceAttributes.FIELD_DESCRIPTION, {})

                method = ImplMethod(method_name)
                method.frequency = method_data.get(ImplMethodAttributes.FREQUENCY, None)
                method.auth_required = not method_data.get(ImplMethodAttributes.NO_AUTH_REQUIRED, False)
                method.is_private = method_data.get(ImplMethodAttributes.PRIVATE, False)
                method.request_limit = method_data.get(ImplMethodAttributes.REQUEST_LIMIT, None)
                method.request_limit = method_data.get(ImplMethodAttributes.TIME_LIMIT, None)
                method.result_type_name = deserialize.SchemaDeserializer._decode_type_string(
                    method_data.get(ImplResourceAttributes.RESULT_TYPE, None))
                method.deprecated = method_data.get(ImplResourceAttributes.DEPRECATED, False)
                method.description = method_data.get(ImplResourceAttributes.DESCRIPTION, '')

                for perm in self._decode_permissions(name, method_name):
                    method.add_permission(perm)

                resource.add_method(method)

                for field_name in fields:
                    field = Deserializer._decode_field(
                        field_name,
                        fields[field_name],
                        fields_descriptions.get(field_name, ''))

                    method.add_field(field)

                for field_name in private_fields:
                    field = Deserializer._decode_field(
                        field_name,
                        private_fields[field_name],
                        fields_descriptions.get(field_name, ''))

                    method.add_private_field(field)

                for query_name in fields_validation:
                    query_data = fields_validation[query_name]
                    for field_name in query_data:
                        field = Deserializer._decode_field(
                            field_name,
                            query_data[field_name],
                            '')

                        method.add_query_field(query_name, field)

        return resource
