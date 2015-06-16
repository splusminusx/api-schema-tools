from models.data_types import ComplexDataType


class Method(ComplexDataType):
    def __init__(self, name, description, result_type_name=None, deprecated=False):
        super(Method, self).__init__(name, description, deprecated)
        self._result_type_name = result_type_name
        self._permissions = {}

    @property
    def result_type_name(self):
        return self._result_type_name

    @result_type_name.setter
    def result_type_name(self, value):
        self._result_type_name = value

    @property
    def permissions(self):
        return self._permissions

    def add_permission(self, permission):
        self._permissions[permission.role] = permission

    def get_permission(self, role):
        return self._permissions[role]
