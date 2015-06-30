#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import io
from storage.schema.serialize import SchemaSerializer
from storage.impl.attrs import ImplResourceAttributes


class MergeSerializer(object):
    def __init__(self, src_path, dest_path):
        self._src_path = src_path
        self._dest_path = dest_path

    @staticmethod
    def _serialize_type(type_name):
        return SchemaSerializer._serialize_type(type_name)

    def _serialize_resource(self, resource):
        with open(os.path.join(self._src_path, u'Methods', resource.name + u'.json')) as input:
            data = json.load(input)

            for method_name in resource.methods:
                method = resource.get_method(method_name)

                if data.get(method_name) is None:
                    data[method_name] = {}
                data[method_name][ImplResourceAttributes.DEPRECATED] = method.deprecated
                data[method_name][ImplResourceAttributes.DESCRIPTION] = method.description
                data[method_name][ImplResourceAttributes.RESULT_TYPE] = self._serialize_type(method.result_type_name)
                data[method_name][ImplResourceAttributes.FIELD_DESCRIPTION] = {}

                for field_name in method.fields:
                    field = method.get_field(field_name)
                    data[method_name][ImplResourceAttributes.FIELD_DESCRIPTION][field_name] = field.description

            with io.open(os.path.join(
                    self._dest_path, u'Methods', resource.name + u'.json'), u'w', encoding='utf-8') as output:
                output.write(unicode(json.dumps(data, ensure_ascii=False, indent=4)))
