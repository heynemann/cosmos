#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

import os
from os.path import expanduser, exists, dirname

import requests
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Credentials:
    def __init__(self, path=None):
        self.path = path
        self.access_token = None
        self.name = None
        self.user_id = None

        if self.path is None:
            self.path = expanduser('~/.config/cosmos/.credentials')

        self.load()

    def to_dict(self):
        return {
            'access_token': self.access_token,
            'user_id': self.user_id,
            'name': self.name
        }

    def load(self):
        if not exists(self.path):
            return

        with open(self.path) as origin:
            obj = load(origin.read(), Loader=Loader)
            if obj is None:
                return
            self.access_token = obj['access_token']

    def save(self):
        if not exists(self.path):
            os.makedirs(dirname(self.path))

        with open(self.path, 'w') as destiny:
            result = dump(self.to_dict(), Dumper=Dumper, default_flow_style=False)
            destiny.write(result)

    def validate(self, token):
        me = requests.get('https://graph.facebook.com/me?access_token=%s' % token)
        if me.status_code != 200:
            raise RuntimeError('Could not authenticate with Facebook. Please try again.')

        obj = me.json()
        self.name = obj['name']
        self.user_id = obj['id']

    def authenticate(self, token):
        self.validate(token)
        self.access_token = token
