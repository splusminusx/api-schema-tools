#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.method import ImplMethod
from models.resource import Resource
from models.field import ValidatableField
from models.validator import *
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

    def resources(self):
        return map(
            lambda x: x.replace(u'.json', u''),
            os.listdir(os.path.join(self._path, u'Methods'))
        )

    @staticmethod
    def _decode_validators(fields):
        validators = []
        for field in fields:
            if field[0] == FieldConstrains.ALLOW_EMPTY:
                validators.append(EmptinessValidator(True))
            if field[0] == FieldConstrains.NON_EMPTY:
                validators.append(EmptinessValidator(False))
            if field[0] == FieldConstrains.REQUIRED:
                validators.append(RequiredFieldValidator.build(field))
            if field[0] == FieldConstrains.ARRAY_OF:
                validators.append(GenericTypeValidation.build(field))
            if field[0] == FieldConstrains.TYPE_OF:
                validators.append(TypeReferenceValidation.build(field))
            if field[0] == FieldConstrains.LENGTH:
                validators.append(LengthValidation.build(field))
            if field[0] == FieldConstrains.MATCH:
                validators.append(MatchValidator.build(field))
            if field[0] == FieldConstrains.DIGIT:
                validators.append(DigitValidation.build(field))
            if field[0] == FieldConstrains.INTEGER:
                validators.append(IntegerValidation.build(field))
            if field[0] == FieldConstrains.ENUM:
                validators.append(EnumValidation.build(field))
            if field[0] == FieldConstrains.FILE:
                validators.append(FileValidation.build(field))
            if field[0] in FieldConstrains.PRIMITIVE_DATA_TYPES:
                validators.append(PrimitiveTypeValidation.build(field))
            if field[0] == FieldConstrains.ID_LIST:
                validators.append(IdListValidation.build(field))
            if field[0] == FieldConstrains.STRING:
                validators.append(StringValidator.build(field))
            if field[0] == FieldConstrains.DATETIME:
                validators.append(DateTimeValidator.build(field))
            if field[0] == FieldConstrains.BOOLEAN:
                validators.append(BooleanValidator.build(field))

    @staticmethod
    def _decode_data_type(validators):
        for val in validators:
            if isinstance(val, GenericTypeValidation):
                return val.type + u'.<' + val.parameter + u'>'
            elif isinstance(val, TypeReferenceValidation):
                return val.type.split(u'\\')[-1]
            elif isinstance(val, DigitValidation):
                return u'numeric'
            elif isinstance(val, IntegerValidation):
                return u'numeric'
            elif isinstance(val, EnumValidation):
                return u'string'
            elif isinstance(val, FileValidation):
                return u'file'
            elif isinstance(val, PrimitiveTypeValidation):
                return val.type_name
            elif isinstance(val, IdListValidation):
                return u'idlist'
            elif isinstance(val, StringValidator):
                return u'string'
            elif isinstance(val, DateTimeValidator):
                return u'datetime'
            elif isinstance(val, BooleanValidator):
                return u'boolean'

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
    def _decode_field(name, fields, validators):
        field_validators = Deserializer._decode_field(fields)

        data_type_name = Deserializer._decode_data_type(field_validators)
        required = Deserializer._decode_required(field_validators)
        default = Deserializer._decode_default(field_validators)

        return ValidatableField(name, data_type_name, '', required, default)

    def decode_resource(self, name):
        resource = Resource(name, u'')
        with open(os.path.join(self._path, u'Methods', name + u'.json')) as f:
            print name
            data = json.load(f)

            for method_name in data:
                print method_name
                method_data = data[method_name]
                fields = method_data.get(ImplMethodAttributes.FIELDS, {})
                fields_validation = method_data.get(
                    ImplMethodAttributes.FIELDS_VALIDATION, {})
                private_fields = method_data.get(
                    ImplMethodAttributes.PRIVATE_FIELDS, {})

                method = ImplMethod(method_name)
                method.frequency = method_data.get(ImplMethodAttributes.FREQUENCY, None)
                method.auth_required = not method_data.get(ImplMethodAttributes.NO_AUTH_REQUIRED, False)
                method.is_private = method_data.get(ImplMethodAttributes.PRIVATE, False)
                method.request_limit = method_data.get(ImplMethodAttributes.REQUEST_LIMIT, None)
                method.request_limit = method_data.get(ImplMethodAttributes.TIME_LIMIT, None)

                resource.add_method(method)

                for field_name in fields:
                    method.add_field(Deserializer._decode_field(
                        field_name,
                        fields[field_name],
                        fields_validation.get(field_name, {})))

                for field_name in private_fields:
                    method.add_private_field(Deserializer._decode_field(
                        field_name,
                        private_fields[field_name],
                        fields_validation.get(field_name, {})))

        return resource
