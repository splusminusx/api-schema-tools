from models.data_types import ComplexDataType


class Method(ComplexDataType):
    def __init__(self, name, description, result_type_name=None, deprecated=False):
        super(Method, self).__init__(name, description, deprecated)
        self._result_type_name = result_type_name
