#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from unittest import TestCase as PythonTestCase


class TestCase(PythonTestCase):
    pass


class ModelTestCase(TestCase):
    @classmethod
    def setup_class(cls):
        import redisco
        redisco.connection_setup(host='localhost', port=4448, db=1)
