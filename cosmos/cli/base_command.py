#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>


import requests
from cliff.command import Command


class RequestError(RuntimeError):
    pass


class BaseCommand(Command):
    def post(self, path, **kw):
        resp = requests.post('http://127.0.0.1:8888%s' % path, data=kw)

        return resp.status_code, resp.text
