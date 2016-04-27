#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>


import tornado.web

from cosmos import logger


class BaseHandler(tornado.web.RequestHandler):
    # def _error(self, status, msg=None):
        # self.set_status(status)
        # if msg is not None:
            # logger.warn(msg)
        # self.finish()
    pass
