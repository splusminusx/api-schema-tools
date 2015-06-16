#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Role(object):
    ADMIN = u'admin'
    ADMIN_PARTNER = u'admin_partner'
    CHIEF = u'chief'
    CHIEF_PARTNER = u'chief_partner'
    MANAGER = u'manager'
    OPERATOR = u'operator'

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
    FULL = 'full'
    MANAGED = 'managed'
    NONE = 'none'
    USER = 'user'

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
        TypeError('Unknown access type: '+string)


class Permission(object):
    def __init__(self, role, access, description=None):
        self._role = role
        self._access = access
        self._description = description

    @property
    def role(self):
        return self._role

    @property
    def access(self):
        return self._access

    @property
    def description(self):
        return self._description
