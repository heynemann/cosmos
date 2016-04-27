#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

import tornado.web
import tornado.ioloop

from cosmos.api.handlers.user import RegisterHandler
from cosmos.api.handlers.healthcheck import HealthcheckHandler


class CosmosApp(tornado.web.Application):

    def __init__(self):
        super(CosmosApp, self).__init__(self.get_handlers())

    def get_handlers(self):
        handlers = [
            (r'/healthcheck', HealthcheckHandler),
            (r'/user/register', RegisterHandler),
        ]

        return handlers
