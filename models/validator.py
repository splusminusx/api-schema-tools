#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
            return [u'allowEmpty']
        else:
            return [u'notEmpty']


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
                return [u'required']
            else:
                return [u'required', {u'default': self.default}]
        else:
            return []

    @staticmethod
    def build(data):


class TypeReferenceValidation(ImplValidator):
    def __init__(self, type, comment):
        super(TypeReferenceValidation, self).__init__(comment)
        self._type = type

    @property
    def type(self):
        return self._type

    def to_impl_schema(self):
        return [u'typeOf', {u'type': self.type}]


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
        return [self.type, {u'type': self.parameter}]


class LengthValidation(MinMaxValidator):
    def __init__(self, min, max, comment):
        super(LengthValidation, self).__init__(min, max, comment)

    def to_impl_schema(self):
        constrains = dict()
        if self._min is not None:
            constrains[u'min'] = self.min
        if self._max is not None:
            constrains[u'max'] = self.max
        return [u'length', constrains]


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


class EnumValidation(ImplValidator):
    def __init__(self, alternatives, comment):
        super(EnumValidation, self).__init__(comment)
        self._alternatives = alternatives

    @property
    def alternatives(self):
        return self._alternatives

    def to_impl_schema(self):
        return [u'enum', self.alternatives]


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
