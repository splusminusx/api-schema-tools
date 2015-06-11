class Resource(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._methods = {}
        self._permissions = {}

    def add_method(self, method):
        self._methods[method.name] = method

    def get_method(self, name):
        return self._name[name]

    def add_permission(self, permission):
        self._permissions[permission.role] = permission

    def get_permission(self, role):
        return self._permissions[role]

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
