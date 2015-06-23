#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.reg import Registry
from storage.impl.deserialize import Deserializer


if __name__ == '__main__':
    reg = Registry()
    deserializer = Deserializer('./schema/implementation')

    for resource_name in deserializer.resources():
        deserializer.decode_resource(resource_name)
