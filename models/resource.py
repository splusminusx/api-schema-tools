class Resource(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._methods = {}

    def add_method(self, method):
        self._methods[method.name] = method

    def get_method(self, name):
        return self._methods[name]

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def methods(self):
        return self._methods
