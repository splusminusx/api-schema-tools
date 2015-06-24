#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Field(object):
    def __init__(self, name, datatypename, description, required):
        self._name = name
        self._datatypename = datatypename
        self._description = description
        self._required = required

    @property
    def name(self):
        return self._name

    @property
    def datatypename(self):
        return self._datatypename

    @property
    def description(self):
        return self._description

    @property
    def required(self):
        return self._required


class ValidatableField(Field):
    def __init__(self, name, datatypename, description, required, default=None):
        super(ValidatableField, self).__init__(name, datatypename, description, required)
        self._validators = []
        self._default = default

    def add_validator(self, validator):
        self._validators.append(validator)

    @property
    def validators(self):
        return self._validators

    @property
    def default(self):
        return self._default
