#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.method import ImplMethod
from models.resource import Resource
from models.field import ValidatableField
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


class FieldConstrains(object):
    # Required

    # Examples:
    #   ['allowEmpty']
    ALLOW_EMPTY = 'allowEmpty'  # можно передать поля без значения, для пустых строк. Для удаления атрибутов.

    # Examples:
    #   ['notEmpty']
    NON_EMPTY = 'notEmpty'  # нельзя передать поля без значения

    # Examples:
    #   ['required']
    #   ['required', {'default': 0}]
    #   ['required', {'default': 'created_at:d'}]
    #   ['required', {'default': 'id:a'}]
    #   ['required', {'default': 'last_name:a'}]
    #   ['required', {'default': 'title:a'}]
    #   ['required', {'default': u'url:a'}]
    #   [['required'], ['string']]
    REQUIRED = 'required'  # обязательно для заполнения, но может быть выставлен default

    # Generic

    # Examples:
    #   ['arrayOf']
    #   ['arrayOf', {'max': 3, 'type': u'App\\Model\\DB\\Billing\\HoldMessage', 'min': 1}]
    #   ['arrayOf', {'type': 'App\\Model\\DB\\Billing\\InvitationRuleSiteBinding'}]
    #   ['arrayOf', {'type': 'App\\Model\\DB\\Billing\\Prechat'}]
    #   ['arrayOf', {'type': 'App\\Model\\DB\\Locations\\Location', 'empty': True}]
    #   ['arrayOf', {'type': 'App\\Model\\Supply\\BatchRequest'}]
    #   ['arrayOf', {'type': 'integer'}]
    ARRAY_OF = 'arrayOf'

    # Examples:
    #   ['typeOf', {'type': '\\App\\Model\\DB\\Billing\\RegistrationMarketingData'}]
    #   ['typeOf', {'type': 'App\\Model\\DB\\CRM\\Contract'}]
    #   ['typeOf', {'type': 'App\\Model\\DB\\Main\\ContactInfo'}]
    #   ['typeOf', {'type': 'App\\Model\\DB\\Payment\\Requisites'}]
    #   ['typeOf', {'type': 'App\\Model\\Supply\\ProductAddition'}]
    #   ['typeOf', {'type': '\\App\\Model\\Supply\\RegistrationPartnerData'}]
    TYPE_OF = 'typeOf'  # сущность в коде с валидаторами для полей.

    # Content

    # Examples:
    #   ['length', {'max': 300}]
    #   ['length', {'min': 6}]
    #   ['length', {'min': 7}]
    LENGTH = 'length'  # ограничение на длину строки

    # Examples:
    #   ['match', {'pattern': '#^(daily|weekly|monthly)$#'}]
    #   ['match', {'pattern': '#^(dark|light|auto)$#'}]
    #   ['match', {'pattern': '#^(email|phone|email_and_phone)$#'}]
    #   ['match', {'pattern': '#^(email|phone|email_or_phone|email_and_phone)$#'}]
    #   ['match', {'pattern': '#^(excluded|specified|home|internal|any)$#'}]
    #   ['match', {'pattern': '#^(form|chat|callback)$#'}]]
    #   ['match', {'pattern': '#^(green|orange|blue|red|purple|gray|rose|black|yellow|white)$#'}]
    #   ['match', {'pattern': '#^(left|right|bottom)$#'}]
    #   ['match', {'pattern': '#^(left|right|bottom|top)$#'}]
    #   ['match', {'pattern': '#^(livetex|visitor)$#'}]
    #   ['match', {'pattern': '#^(man|woman|operator|custom)$#'}]
    #   ['match', {'pattern': '#^(missed|completed)$#'}]
    #   ['match', {'pattern': '#^(missed|completed)$#'}]
    #   ['match', {'pattern': '#^(none|custom)$#'}]
    #   ['match', {'pattern': '#^(none|default|custom)$#'}]
    #   ['match', {'pattern': '#^(now|after_current|after_payment)$#'}]
    #   ['match', {'pattern': '#^(offline|online|busy)$#'}]
    #   ['match', {'pattern': '/^(online|offline|busy)$/'}]
    #   ['match', {'pattern': '#^(pixel|percent)$#'}]
    #   ['match', {'pattern': '#^(positive|negative|undefined)$#'}]
    #   ['match', {'pattern': '#^(predefined|custom)$#'}]
    #   ['match', {'pattern': '#^(preset|custom)$#'}]
    #   ['match', {'pattern': '#^ru_person|ru_legal|ua_person|ua_legal|ua_sp$#'},
    #       None, "payer_type must be one of 'ru_person', 'ru_legal', 'ua_person', 'ua_legal', 'ua_sp'"]
    #   ['match', {'pattern': '#^(sip|phone)$#'}]
    #   ['match', {'pattern': '#^(small|large)$#'}]
    #   ['match', {'pattern': '#^(small|middle|large)$#'}]
    #   ['match', {'pattern': '#^(submitted|inprogress|w4lt|w4e|closed)$#'}]
    #   ['match', {'pattern': '#^(top|right|bottom|left)$#'}]
    #   ['match', {'pattern': '#^(undefined|incident|request)$#'}]
    #   ['match', {'pattern': '#^(undefined|low|normal|high|critical)$#'}]
    #   ['match', {'pattern': '#^(vary|chat|lead)$#'}]
    #   ['match', {'pattern': '#^(visitor|employee)$#'}]
    #   ['match', {'pattern': '#^(xwidget|call_from_site)$#'}]
    MATCH = 'match'  # любая регулярка

    # WTF?????
    # Examples:
    #   ['upload']
    UPLOAD = 'upload'  # в паре с field идентификатор поля в сущности для загрузки содержимого файла

    # Non specified data types

    # Examples:
    #   ['digit']
    #   ['digit', {'max': 100, 'min': -15}]
    DIGIT = 'digit'  # может быть float или int

    # Examples:
    #   ['integer']
    #   ['integer', {'max': 1000}, None, 'Значение должно быть меньше 1000']
    #   ['integer', {'max': 100}, None, 'Значение должно быть меньше 100']
    #   ['integer', {'max': 3600, 'min': 5}, None, 'Значение должно быть от 5 до 3600']
    INTEGER = 'integer'  # только int

    # Examples:
    #   ['enum', ['acceptance', 'invoice', 'vatinvoice']]
    #   ['enum', ['chat', 'lead', 'complaint']]
    #   ['enum', ['employee', 'visitor']]
    #   ['enum', ['vary', 'chat', 'lead']]
    ENUM = 'enum'  # массив со значениями из enum'а

    # Specified data types

    # Examples:
    #   ['boolean']
    BOOLEAN = 'boolean'

    # Examples:
    #   ['color']
    COLOR = 'color'

    # Examples:
    #   ['currency']
    CURRENCY = 'currency'

    # Examples:
    #   ['email']
    #   ['email', {'empty': True}]
    EMAIL = 'email'

    # Examples:
    #   ['file', {'empty': True, 'entity': ['callButton.image_offline']}]
    #   ['file', {'empty': True, 'entity': ['callButton.image_online']}]
    #   ['file', {'empty': True, 'entity': ['chatButton.image_offline']}]
    #   ['file', {'empty': True, 'entity': ['chatButton.image_online']}]
    #   ['file', {'entity': ['employee.photo']}]
    #   ['file', {'entity': ['payer.acceptance']}]
    #   ['file', {'entity': ['siteCallSettings.background_custom']}]
    #   ['file', {'entity': ['siteCallSettings.greeting_custom']}]
    #   ['file', {'entity': ['siteWidgetSettings.banner_custom']}]
    #   ['file', {'entity': ['siteWidgetSettings.invitation_photo_custom']}]
    FILE = 'file'

    # Examples:
    #   ['idList']
    #   ['idList']
    #   ['idList', {'pattern': '#^(missed|completed)$#', 'type': 'string'}]
    #   ['idList', {'type': 'integer'}]
    #   ['idlist', {'type': 'string'}]]
    #   ['idList', {'type': 'string'}]
    ID_LIST = 'idList'

    # Examples:
    #   ['phone']
    PHONE = 'phone'

    #  Examples:
    #    ['string']
    #    ['string']
    #    ['string', {'length': 100}]
    #    ['string', {'length': 180}]
    #    ['string', {'length': 2000}]
    #    ['string', {'length': 60}]
    #    [['string'], ['match', {'pattern': u'#^(sip|phone)$#'}]]
    STRING = 'string'

    # Specified only for fields validation

    # Examples:
    #    ['date']
    DATE = 'date'

    # Examples:
    #   [['datetime']]
    #   [['datetime', {'max': '1 month'}]]
    #   [['datetime', {'max': '30 days'}, None, 'Максимально возможный интервал - 30 дней']]
    DATETIME = 'datetime'

    # Example:
    #   ['time']
    TIME = 'time'

    # Unspecified
    # NUMERIC = 'numeric' мапиться на digit и integer

    _TYPE_CONSTRAINS = [
        BOOLEAN,
        COLOR,
        CURRENCY,
        EMAIL,
        FILE,
        ID_LIST,
        PHONE,
        STRING,
        DATE,
        DATETIME,
        TIME,
        DIGIT,
        INTEGER,
        ENUM
    ]

    @staticmethod
    def is_type_constrain(constrain):
        return constrain in FieldConstrains._TYPE_CONSTRAINS


class Deserializer(object):
    def __init__(self, path):
        self._path = path

    def resources(self):
        return map(
            lambda x: x.replace(u'.json', u''),
            os.listdir(os.path.join(self._path, u'Methods'))
        )

    @staticmethod
    def _decode_field(name, fields, validators):
        data_type_name = None
        required = False
        for field in fields:
            if FieldConstrains.is_type_constrain(field[0]):
                data_type_name = field[0]
            if field[0] == FieldConstrains.REQUIRED:
                required = True
            if field[0] == FieldConstrains.ARRAY_OF:
                if field[1]:
                    data_type_name = 'Array.<' + field[1]['type'] + '>'
                else:
                    data_type_name = 'Array.<string>'

        if data_type_name:
            return ValidatableField(name, data_type_name, '', required)

        for field in fields:
            if field[0] == FieldConstrains.MATCH:
                data_type_name = 'string'

        if data_type_name:
            return ValidatableField(name, data_type_name, '', required)
        else:
            raise ValueError('Can not understand field "' + name + '" type.')

    def decode_resource(self, name):
        with open(os.path.join(self._path, u'Methods', name + u'.json')) as f:
            print name
            data = json.load(f)
            resource = Resource(name, u'')

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
                    method.add_field(self._decode_field(
                        field_name,
                        fields[field_name],
                        fields_validation.get(field_name, {})))

                for field_name in private_fields:
                    method.add_private_field(self._decode_field(
                        field_name,
                        private_fields[field_name],
                        fields_validation.get(field_name, {})))
