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


class ImplMethod(Method):
    def __init__(self, name, description='', result_type_name=None, deprecated=False):
        super(ImplMethod, self).__init__(name, description, result_type_name, deprecated)
        self._frequency = None
        self._auth_required = True
        self._private_fields = {}
        self._is_private = False
        self._request_limit = None
        self._time_limit = None

    @property
    def is_private(self):
        return self._is_private

    @is_private.setter
    def is_private(self, value):
        self._is_private = value

    @property
    def auth_required(self):
        return self._auth_required

    @auth_required.setter
    def auth_required(self, value):
        self._auth_required = value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        self._frequency = value

    @property
    def request_limit(self):
        return self._request_limit

    @request_limit.setter
    def request_limit(self, value):
        self._request_limit = value

    @property
    def time_limit(self):
        return self._time_limit

    @time_limit.setter
    def time_limit(self, value):
        self._time_limit = value

    def add_private_field(self, field):
        self._private_fields[field.name] = field

    def get_private_field(self, field_name):
        return self._private_fields[field_name]
