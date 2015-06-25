#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FieldConstrains(object):
    # Required

    # Examples:
    #   ['allowEmpty']
    #
    # [+] - EmptinessValidator
    #
    # public function allowEmpty($value)
    ALLOW_EMPTY = 'allowEmpty'  # можно передать поля без значения, для пустых строк. Для удаления атрибутов.

    # Examples:
    #   ['notEmpty']
    #
    # [+] - EmptinessValidator
    #
    # public function notEmpty($value)
    NON_EMPTY = 'notEmpty'  # нельзя передать поля без значения

    # Examples:
    #   ['required']
    #   ['required', {'default': 0}]
    #   ['required', {'default': 'created_at:d'}]
    #   ['required', {'default': 'id:a'}]
    #   ['required', {'default': 'last_name:a'}]
    #   ['required', {'default': 'title:a'}]
    #   ['required', {'default': 'url:a'}]
    #   [['required'], ['string']]
    #
    # [+] - ValidatableField - args: default, required
    #
    # public function required($value, $params = ['default' => null])
    REQUIRED = 'required'  # обязательно для заполнения, но может быть выставлен default

    # Generic

    # Examples:
    #   ['arrayOf'] -> модифицируем в ['arrayOf', {'type': 'string'}]
    #   ['arrayOf', {'max': 3, 'type': u'App\\Model\\DB\\Billing\\HoldMessage', 'min': 1}]
    #   ['arrayOf', {'type': 'App\\Model\\DB\\Billing\\InvitationRuleSiteBinding'}]
    #   ['arrayOf', {'type': 'App\\Model\\DB\\Billing\\Prechat'}]
    #   ['arrayOf', {'type': 'App\\Model\\DB\\Locations\\Location', 'empty': True}]
    #   ['arrayOf', {'type': 'App\\Model\\Supply\\BatchRequest'}]
    #   ['arrayOf', {'type': 'integer'}]
    #
    # [+] ImplTypeValidator, MinMaxValidator, EmptinessValidator
    ARRAY_OF = 'arrayOf'

    # Examples:
    #   ['typeOf', {'type': '\\App\\Model\\DB\\Billing\\RegistrationMarketingData'}]
    #   ['typeOf', {'type': 'App\\Model\\DB\\CRM\\Contract'}]
    #   ['typeOf', {'type': 'App\\Model\\DB\\Main\\ContactInfo'}]
    #   ['typeOf', {'type': 'App\\Model\\DB\\Payment\\Requisites'}]
    #   ['typeOf', {'type': 'App\\Model\\Supply\\ProductAddition'}]
    #   ['typeOf', {'type': '\\App\\Model\\Supply\\RegistrationPartnerData'}]
    #
    # [-] ImplTypeValidator
    TYPE_OF = 'typeOf'  # сущность в коде с валидаторами для полей.

    # Content

    # Examples:
    #   ['length', {'max': 300}]
    #   ['length', {'min': 6}]
    #   ['length', {'min': 7}]
    #
    # [+] - MinMaxValidator
    #
    # public function length($value, $params = ['min' => 0, 'max' => null])
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
    #
    # [+] - MatchValidator
    #
    # public function match($value, $params = ['pattern' => '#.*#'])
    MATCH = 'match'  # любая регулярка

    # WTF?????
    # Examples:
    #   ['upload']
    #
    # [-]
    #
    # public function upload($value)
    UPLOAD = 'upload'  # в паре с field идентификатор поля в сущности для загрузки содержимого файла

    # Non specified data types

    # Examples:
    #   ['digit']
    #   ['digit', {'max': 100, 'min': -15}]
    #
    # [+] MinMaxValidator, ImplTypeValidator
    #
    # public function digit($value, $params = ['min' => null, 'max' => null])
    DIGIT = 'digit'  # может быть float или int

    # Examples:
    #   ['integer']
    #   ['integer', {'max': 1000}, None, 'Значение должно быть меньше 1000']
    #   ['integer', {'max': 100}, None, 'Значение должно быть меньше 100']
    #   ['integer', {'max': 3600, 'min': 5}, None, 'Значение должно быть от 5 до 3600']
    #
    # [+] MinMaxValidator, MinMaxValidator
    #
    # public function integer($value, $params = ['min' => null, 'max' => null])
    INTEGER = 'integer'  # только int

    # Examples:
    #   ['enum', ['acceptance', 'invoice', 'vatinvoice']]
    #   ['enum', ['chat', 'lead', 'complaint']]
    #   ['enum', ['employee', 'visitor']]
    #   ['enum', ['vary', 'chat', 'lead']]
    #
    # [+] ImplTypeValidator
    #
    # public function enum($value, $allowedValues = [])
    ENUM = 'enum'  # массив со значениями из enum'а

    # Specified data types

    # Examples:
    #   ['boolean']
    #
    # public function boolean($value, $params = ['strict' => false])
    BOOLEAN = 'boolean'

    # Examples:
    #   ['color']
    COLOR = 'color'

    # Examples:
    #   ['currency']
    #
    # public function currency($value)
    CURRENCY = 'currency'

    # Examples:
    #   ['email']
    #   ['email', {'empty': True}]
    #
    # [+] - EmptinessValidator
    #
    # public function email($value, $params = ['empty' => false])
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
    #
    # [+] - EmptinessValidator,
    #
    # public function file($value, $params)
    # params: empty, entity
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
    #
    # public function string($value, $param = ['length' => 2000])
    STRING = 'string'

    # public function text($value, $param = ['length' => 10000])
    TEXT = 'text'

    # Specified only for fields validation

    # Examples:
    #    ['date']
    #
    # public function date($value)
    DATE = 'date'

    # Examples:
    #   [['datetime']]
    #   [['datetime', {'max': '1 month'}]]
    #   [['datetime', {'max': '30 days'}, None, 'Максимально возможный интервал - 30 дней']]
    #
    # public function datetime($value)
    DATETIME = 'datetime'

    # Example:
    #   ['time']
    #
    # public function time($value)
    TIME = 'time'

    # Unspecified
    # NUMERIC = 'numeric' мапиться на digit и integer

    _TYPE_CONSTRAINS = [
        ARRAY_OF,
        TYPE_OF,
        UPLOAD,
        DIGIT,
        INTEGER,
        ENUM,
        BOOLEAN,
        COLOR,
        CURRENCY,
        EMAIL,
        FILE,
        ID_LIST,
        PHONE,
        TEXT,
        DATE,
        DATETIME,
        TIME
    ]

    PRIMITIVE_DATA_TYPES = [
        UPLOAD,
        COLOR,
        CURRENCY,
        EMAIL,
        PHONE,
        DATE,
        TIME
    ]

    _VALUE_CONSTRAINS = [
        ALLOW_EMPTY,
        NON_EMPTY,
        REQUIRED,
        LENGTH,
        MATCH
    ]

    DEFAULT = 'string'

    @staticmethod
    def is_type_constrain(constrain):
        return constrain in FieldConstrains._TYPE_CONSTRAINS

    @staticmethod
    def is_value_constrain(constrain):
        return constrain in FieldConstrains._VALUE_CONSTRAINS


class ImplValidator(object):
    def __init__(self, comment):
        self._comment = comment

    @property
    def comment(self):
        return self._comment

    def to_impl_schema(self):
        pass


class EmptyImplValidator(ImplValidator):
    def __init__(self, empty, comment):
        super(EmptyImplValidator).__init__(comment)
        self._empty = empty

    @property
    def empty(self):
        return self._empty


class MinMaxValidator(ImplValidator):
    def __init__(self, min, max, comment):
        super(MinMaxValidator).__init__(comment)
        self._min = min
        self._max = max

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max


# Проверка пустоты поля
class EmptinessValidator(EmptyImplValidator):
    def __init__(self, empty, comment=None):
        super(EmptinessValidator, self).__init__(empty, comment)

    def to_impl_schema(self):
        if self.empty is None:
            return []
        if self.empty:
            return [FieldConstrains.ALLOW_EMPTY]
        else:
            return [FieldConstrains.NON_EMPTY]


# Проверка обязательности поля
class RequiredFieldValidator(ImplValidator):
    def __init__(self, required, default, comment):
        super(RequiredFieldValidator, self).__init__(comment)
        self._required = required
        self._default = default

    @property
    def required(self):
        return self._required

    @property
    def default(self):
        return self._default

    def to_impl_schema(self):
        if self._required:
            if self._default is None:
                return [FieldConstrains.REQUIRED]
            else:
                return [FieldConstrains.REQUIRED, {u'default': self.default}]
        else:
            return []

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.REQUIRED:
            default = None
            if len(data) > 1:
                default = data[1].get(u'default', None)
            return RequiredFieldValidator(True, default, None)
        else:
            raise ValueError('Validator type must be "' +
                             FieldConstrains.REQUIRED + '", found: ' + data[0])


class TypeReferenceValidation(ImplValidator):
    def __init__(self, type, comment):
        super(TypeReferenceValidation, self).__init__(comment)
        self._type = type

    @property
    def type(self):
        return self._type

    def to_impl_schema(self):
        return [FieldConstrains.TYPE_OF, {u'type': self.type}]

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.TYPE_OF:
            type = FieldConstrains.DEFAULT
            if len(data) > 1:
                type = data[1].get(u'type', FieldConstrains.DEFAULT)
            return TypeReferenceValidation(type, None)
        else:
            raise ValueError('Validator type must be "' +
                             FieldConstrains.TYPE_OF + '", found: ' + data[0])


class GenericTypeValidation(EmptyImplValidator, MinMaxValidator, TypeReferenceValidation):
    def __init__(self, type, parameter, **kwargs):
        TypeReferenceValidation.__init__(self, type, kwargs.get(u'comment', None))
        EmptyImplValidator.__init__(self, kwargs.get(u'empty', None), kwargs.get(u'comment', None))
        MinMaxValidator.__init__(
            self, kwargs.get(u'min', None), kwargs.get(u'max', None), kwargs.get(u'comment', None))
        self._parameter = parameter

    @property
    def parameter(self):
        return self._parameter

    def to_impl_schema(self):
        result = []

        if self.type == u'Array':
            result.append(FieldConstrains.ARRAY_OF)
        else:
            result.append(self.type)

        params = {u'type': self.parameter}
        if self.min is not None:
            params[u'min'] = self.min
        if self.min is not None:
            params[u'max'] = self.max
        if self.empty is not None:
            params[u'empty'] = self.empty
        if self.empty is not None:
            params[u'empty'] = self.empty

        if len(params) > 0:
            result.append(params)
            if self.comment is not None:
                result.append(None)
                result.append(self.comment)

        return result

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.ARRAY_OF:
            parameter = FieldConstrains.DEFAULT
            empty = None
            max = None
            min = None
            comment = None
            if len(data) > 1:
                parameter = data[1].get(u'type', FieldConstrains.DEFAULT)
                empty = data[1].get(u'empty', None)
                max = data[1].get(u'max', None)
                min = data[1].get(u'min', None)
            if len(data) > 3:
                comment = data[3]
            return GenericTypeValidation(
                u'Array',
                parameter,
                min=min,
                max=max,
                comment=comment,
                empty=empty
            )
        else:
            raise ValueError('Validator type must be "' +
                             FieldConstrains.ARRAY_OF + '", found: ' + data[0])


class LengthValidation(MinMaxValidator):
    def __init__(self, min, max, comment):
        super(LengthValidation, self).__init__(min, max, comment)

    def to_impl_schema(self):
        constrains = dict()
        if self._min is not None:
            constrains[u'min'] = self.min
        if self._max is not None:
            constrains[u'max'] = self.max
        return [FieldConstrains.LENGTH, constrains]

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.LENGTH:
            min = None
            max = None
            if len(data) > 1:
                min = data[1].get(u'min', None)
                max = data[1].get(u'max', None)
            return LengthValidation(min, max, None)
        else:
            ValueError('Validator type must be "' +
                       FieldConstrains.LENGTH + '", found: ' + data[0])


class MatchValidator(ImplValidator):
    def __init__(self, pattern, comment):
        super(MatchValidator, self).__init__(comment)
        self._pattern = pattern

    @property
    def pattern(self):
        return self._pattern

    def to_impl_schema(self):
        if self.comment is not None:
            return [u'match', {u'pattern': self.pattern}, None, self.comment]
        else:
            return [u'match', {u'pattern': self.pattern}]

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.MATCH:
            pattern = None
            comment = None
            if len(data) > 1:
                pattern = data[1]
            if len(data) > 3:
                comment = data[3]
            return MatchValidator(pattern, comment)
        else:
            raise ValueError('Validator type must be "' +
                             FieldConstrains.MATCH + '", found: ' + data[0])


class DigitValidation(MinMaxValidator):
    def __init__(self, min, max, comment):
        super(DigitValidation, self).__init__(min, max, comment)

    def to_impl_schema(self):
        if self.min is not None or self.max is not None:
            constrains = dict()
            if self._min is not None:
                constrains[u'min'] = self.min
            if self._max is not None:
                constrains[u'max'] = self.max
            return [u'digit', constrains]
        else:
            return [u'digit']

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.DIGIT:
            min = None
            max = None
            if len(data) > 1:
                min = data[1].get(u'min', None)
                max = data[1].get(u'max', None)
            return DigitValidation(min, max, None)
        else:
            raise ValueError('Validator type must be "' +
                             FieldConstrains.DIGIT + '", found: ' + data[0])


class IntegerValidation(MinMaxValidator):
    def __init__(self, min, max, comment):
        super(IntegerValidation, self).__init__(min, max, comment)

    def to_impl_schema(self):
        result = [u'integer']
        if self.min is not None or self.max is not None:
            constrains = dict()
            if self._min is not None:
                constrains[u'min'] = self.min
            if self._max is not None:
                constrains[u'max'] = self.max
            result.append(constrains)
        if self.comment is None:
            result.append(None)
            result.append(self.comment)

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.INTEGER:
            min = None
            max = None
            comment = None
            if len(data) > 1:
                min = data[1].get(u'min', None)
                max = data[1].get(u'max', None)
            if len(data) > 3:
                comment = data[1].get(u'comment', None)
            return IntegerValidation(min, max, comment)
        else:
            raise ValueError('Validator type must be "' +
                             FieldConstrains.INTEGER + '", found: ' + data[0])


class EnumValidation(ImplValidator):
    def __init__(self, alternatives, comment):
        super(EnumValidation, self).__init__(comment)
        self._alternatives = alternatives

    @property
    def alternatives(self):
        return self._alternatives

    def to_impl_schema(self):
        return [u'enum', self.alternatives]

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.INTEGER:
            alternatives = []
            if len(data) > 1:
                alternatives = data[1]
            return EnumValidation(alternatives, None)
        else:
            raise ValueError('Validator type must be "' +
                             FieldConstrains.ENUM + '", found: ' + data[0])


class PrimitiveTypeValidation(EmptyImplValidator):
    def __init__(self, type_name, empty=None, comment=None):
        super(PrimitiveTypeValidation, self).__init__(empty, comment)
        self._type_name = type_name

    @property
    def type_name(self):
        return self._type_name

    def to_impl_schema(self):
        if self.empty is None:
            return [self._type_name]
        else:
            return [self._type_name, {u'empty': self.empty}]

    @staticmethod
    def build(data):
        type_name = data[0]
        if type_name in FieldConstrains.PRIMITIVE_DATA_TYPES:
            empty = None
            if len(data) > 1:
                empty = data[1].get(u'empty', None)
            return PrimitiveTypeValidation(type_name, empty, None)
        else:
            raise ValueError(u'Validator type must be in"' +
                             unicode(FieldConstrains.PRIMITIVE_DATA_TYPES) +
                             u'", found: ' + type_name)


class FileValidation(EmptyImplValidator):
    def __init__(self, field, empty=None, comment=None):
        super(FileValidation, self).__init__(empty, comment)
        self._field = field

    @property
    def field(self):
        return self._field

    def to_impl_schema(self):
        if self.empty is None:
            return [u'file', {u'entity': self.field}]
        else:
            return [u'file', {u'entity': self.field, u'empty': self.empty}]

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.FILE:
            field = None
            empty = None
            if len(data) > 1:
                field = data[1].get(u'entity', None)
                empty = data[1].get(u'empty', None)
            return FileValidation(field, empty, None)
        else:
            raise ValueError(u'Validator type must be in"' +
                             FieldConstrains.FILE +
                             u'", found: ' + data[0])


class IdListValidation(TypeReferenceValidation):
    def __init__(self, type=None, pattern=None, comment=None):
        super(IdListValidation, self).__init__(type, comment)
        self._pattern = pattern

    @property
    def pattern(self):
        return self._pattern

    def to_impl_schema(self):
        constrains = dict()
        if self.pattern is not None:
            constrains[u'pattern'] = self.pattern
        if self.type is not None:
            constrains[u'type'] = self.type
        if len(constrains) > 0:
            return [u'idList', constrains]
        else:
            return [u'idList']

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.ID_LIST:
            pattern = None
            type = None
            if len(data) > 1:
                pattern = data[1].get(u'pattern', None)
                type = data[1].get(u'type', None)
            return IdListValidation(type, pattern, None)
        else:
            raise ValueError(u'Validator type must be in"' +
                             FieldConstrains.ID_LIST +
                             u'", found: ' + data[0])


class StringValidator(ImplValidator):
    def __init__(self, length, comment):
        super(StringValidator, self).__init__(comment)
        self._length = length

    @property
    def length(self):
        return self._length

    def to_impl_schema(self):
        constrains = dict()
        if self.length is not None:
            constrains[u'length'] = self.length
        if len(constrains) > 0:
            return [u'string', constrains]
        else:
            return [u'string']

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.STRING:
            length = None
            if len(data) > 1:
                length = data[1].get(u'length', None)
            return StringValidator(length, None)
        else:
            ValueError(u'Validator type must be in"' +
                       FieldConstrains.STRING +
                       u'", found: ' + data[0])


class DateTimeValidator(MinMaxValidator):
    def __init__(self, min, max, comment):
        super(DateTimeValidator, self).__init__(min, max, comment)
        self._comment = comment

    def to_impl_schema(self):
        result = [u'datetime']
        if self.min is not None or self.max is not None:
            constrains = dict()
            if self._min is not None:
                constrains[u'min'] = self.min
            if self._max is not None:
                constrains[u'max'] = self.max
            result.append(constrains)
        if self.comment is None:
            result.append(None)
            result.append(self.comment)

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.DATETIME:
            max = None
            min = None
            comment = None
            if len(data) > 1:
                max = data[1].get(u'max', None)
                min = data[1].get(u'min', None)
            if len(data) > 3:
                comment = data[3]
            return DateTimeValidator(
                min=min,
                max=max,
                comment=comment,
            )
        else:
            ValueError(u'Validator type must be in"' +
                       FieldConstrains.DATETIME +
                       u'", found: ' + data[0])


class BooleanValidator(ImplValidator):
    def __init__(self, strict=None, comment=None):
        super(BooleanValidator, self).__init__(comment)
        self._strict = strict

    @property
    def strict(self):
        return self._strict

    def to_impl_schema(self):
        if self.strict is not None:
            return [u'boolean', {u'strict': self.strict}]
        else:
            return [u'boolean']

    @staticmethod
    def build(data):
        if data[0] == FieldConstrains.BOOLEAN:
            strict = None
            if len(data) > 1:
                strict = data[1].get(u'strict', None)
            return BooleanValidator(strict, None)
        else:
            ValueError(u'Validator type must be in"' +
                       FieldConstrains.BOOLEAN +
                       u'", found: ' + data[0])
