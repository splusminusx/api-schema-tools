#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Registry(object):
    def __init__(self):
        self._registry = {}

    def add_type(self, data_type):
        self._registry[data_type.name] = data_type

    def get_type(self, name):
        return self._registry[name]

    def type_defined(self, name):
        return name in self._registry

    @property
    def types(self):
        return self._registry
