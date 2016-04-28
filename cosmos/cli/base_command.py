#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>


import logging

import requests
from cliff.command import Command

from cosmos.cli.credentials import Credentials


class RequestError(RuntimeError):
    pass


class BaseCommand(Command):
    def __init__(self, *args, **kw):
        super(BaseCommand, self).__init__(*args, **kw)
        self.credentials = Credentials()
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

    def say(self, message):
        self.app.stdout.write("%s\n" % message)

    def validate_user(self):
        self.credentials.validate(self.credentials.access_token)

    def post(self, path, **kw):
        resp = requests.post('http://127.0.0.1:8888%s' % path, data=kw)

        return resp.status_code, resp.text
