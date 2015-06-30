#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Role(object):
    ADMIN = u'admin'
    ADMIN_PARTNER = u'admin_partner'
    CHIEF = u'chief'
    CHIEF_PARTNER = u'chief_partner'
    MANAGER = u'manager'
    OPERATOR = u'operator'

    ROLES = [
        ADMIN,
        ADMIN_PARTNER,
        CHIEF,
        CHIEF_PARTNER,
        MANAGER,
        OPERATOR
    ]

    @classmethod
    def get_role(cls, string):
        if string.find(u'Администратор') != -1:
            if string.find(u'admin_partner') != -1:
                return cls.ADMIN_PARTNER
            else:
                return cls.ADMIN
        if string.find(u'Управляющий') != -1:
            if string.find(u'chief_partner') != -1:
                return cls.CHIEF_PARTNER
            else:
                return cls.CHIEF
        if string.find(u'Руководитель операторов') != -1:
            return cls.MANAGER
        if string.find(u'Оператор') != -1:
            return cls.OPERATOR
        TypeError('Unknown role type: '+string)


class Access(object):
    FULL = u'full'
    MANAGED = u'managed'
    NONE = u'none'
    ROUTED = u'routed'
    USER = u'user'

    @classmethod
    def get_access(cls, string):
        if string.find(u'full') != -1:
            return cls.FULL
        if string.find(u'managed') != -1:
            return cls.MANAGED
        if string.find(u'none') != -1:
            return cls.NONE
        if string.find(u'user') != -1:
            return cls.USER
        if string.find(u'routed') != -1:
            return cls.ROUTED
        TypeError('Unknown access type: '+string)


class Permission(object):
    def __init__(self, role, access, description=None):
        self._role = role
        self._access = access
        self._description = description
        self._fields = []
        self._is_allow_all_fields = False

    @property
    def role(self):
        return self._role

    @property
    def access(self):
        return self._access

    @property
    def description(self):
        return self._description

    def add_field(self, field):
        self._fields.append(field)

    @property
    def fields(self):
        return self._fields

    @property
    def is_allow_all_fields(self):
        return self._is_allow_all_fields

    @is_allow_all_fields.setter
    def is_allow_all_fields(self, value):
        self._is_allow_all_fields = value

