#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.field import Field


class PrimitiveDataType(object):
    def __init__(self, name, description, deprecated=False):
        self._name = name
        self._description = description
        self._deprecated = deprecated

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def deprecated(self):
        return self._deprecated


class ComplexDataType(PrimitiveDataType):
    def __init__(self, name, description, deprecated=False):
        super(ComplexDataType, self).__init__(name, description, deprecated)
        self._fields = {}

    def add_field(self, name, datatypename, description, required=False):
        self._fields[name] = Field(name, datatypename, description, required)

    def get_field(self, name):
        return self._fields[name]

    def has_field(self, name):
        return name in self._fields

    @property
    def fields(self):
        return self._fields
