#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from cosmos.api.handlers import BaseHandler


class HealthcheckHandler(BaseHandler):
    def get(self):
        self.write('WORKING')

    def head(self, *args, **kwargs):
        self.set_status(200)
