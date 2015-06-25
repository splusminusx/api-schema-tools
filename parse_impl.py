#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.reg import Registry
from storage.impl.deserialize import Deserializer
from storage.schema.deserialize import SchemaDeserializer
from pprint import pprint


if __name__ == '__main__':
    impl_reg = Registry()
    resource_reg = Registry()
    type_reg = Registry()

    impl_deserializer = Deserializer('./schema/implementation')
    spec_deserializer = SchemaDeserializer('./schema')

    for resource_name in impl_deserializer.resources():
        impl_reg.add_type(impl_deserializer.decode_resource(resource_name))

    for type_name in spec_deserializer.types():
        type_reg.add_type(spec_deserializer.decode_type(type_name))

    for resource_name in spec_deserializer.resources():
        resource_reg.add_type(spec_deserializer.decode_resource(resource_name))

    spec_resource_names = set(resource_reg.types.keys())
    impl_resource_names = set(impl_reg.types.keys())
    print "\n>>> Unimplemented resources:"
    pprint(spec_resource_names.difference(impl_resource_names))
    print "\n>>> Unspecified resources:"
    pprint(impl_resource_names.difference(spec_resource_names))

    spec_methods = []
    spec_fields = {}
    impl_methods = []
    impl_fields = {}
    for rn in spec_resource_names.intersection(impl_resource_names):
        spec_resource = resource_reg.get_type(rn)
        for mn in spec_resource.methods:
            spec_methods.append(rn + '.' + mn)

        impl_resource = impl_reg.get_type(rn)
        for mn in impl_resource.methods:
            impl_methods.append(rn + '.' + mn)

        for mn in set(spec_resource.methods).intersection(set(impl_resource.methods)):
            spec_method = spec_resource.get_method(mn)
            for fn in spec_method.fields:
                spec_fields[rn + '.' + mn + '.' + fn] = spec_method.get_field(fn)

            impl_method = impl_resource.get_method(mn)
            for fn in impl_method.fields:
                impl_fields[rn + '.' + mn + '.' + fn] = impl_method.get_field(fn)

    print "\n>>> Unimplemented methods:"
    pprint(set(spec_methods).difference(set(impl_methods)))
    print "\n>>> Unspecified methods:"
    pprint(set(impl_methods).difference(set(spec_methods)))

    print "\n>>> Unimplemented fields:"
    pprint(set(spec_fields.keys()).difference(set(impl_fields.keys())))
    print "\n>>> Unspecified fields:"
    pprint(set(impl_fields.keys()).difference(set(spec_fields.keys())))

    print "\n>>> Incorrect field type:"
    for fn in set(spec_fields.keys()).intersection(set(impl_fields.keys())):
        if spec_fields[fn].datatypename != impl_fields[fn].datatypename:
            print fn + ' ::', 'spec=' + spec_fields[fn].datatypename, 'impl=' + impl_fields[fn].datatypename

    print "\n>>> Incorrect requirement modifier:"
    for fn in set(spec_fields.keys()).intersection(set(impl_fields.keys())):
        if spec_fields[fn].required != impl_fields[fn].required:
            print fn + ' ::', 'spec=' + str(spec_fields[fn].required), 'impl=' + str(impl_fields[fn].required)
