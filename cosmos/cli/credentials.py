#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

import os
from os.path import expanduser, exists, dirname
import logging

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
        self.current_target = None
        self.targets = {}

        if self.path is None:
            self.path = expanduser('~/.config/cosmos/.credentials')

        self.load()

    def to_dict(self):
        return {
            'access_token': self.access_token,
            'user_id': self.user_id,
            'name': self.name,
            'current_target': self.current_target,
            'targets': self.targets,
        }

    def from_dict(self, values):
        for key, value in values.items():
            setattr(self, key, value)

    def load(self):
        if not exists(self.path):
            return

        with open(self.path) as origin:
            obj = load(origin.read(), Loader=Loader)
            if obj is None:
                return
            self.from_dict(obj)

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

    def validate_target(self, name, url, raises=True):
        try:
            working = requests.get('%s/healthcheck' % url.rstrip('/'))
        except requests.exceptions.HTTPError as e:
            if raises:
                raise RuntimeError('Could not reach target "%s". Error: %s' % (url, e.message))
            return False
        except requests.exceptions.ConnectionError as e:
            if raises:
                raise RuntimeError('Could not reach target "%s". Error: %s' % (url, e.message))
            return False

        if working.status_code != 200 or working.text != 'WORKING':
            if raises:
                raise RuntimeError('Could not reach target "%s". Error: %s' % (url, working.text))
            return False

        return True

    def target_add(self, name, url):
        if name in self.targets:
            raise RuntimeError('Target %s is already registered. Try "cosmos target-remove %s" first!' % (
                name, name
            ))

        try:
            self.validate_target(name, url)
        except RuntimeError, err:
            logging.warn(str(err))

        self.targets[name] = url

    def validate_target_exists(self, name):
        if name not in self.targets:
            raise RuntimeError('Target %s was not found. Try "cosmos target-add %s <url>" first!' % (
                name, name
            ))

    def target_remove(self, name):
        self.validate_target_exists(name)
        del self.targets[name]

    def target_set(self, name):
        self.validate_target_exists(name)
        self.current_target = name

    def set_target(self, target_url):
        self.target_url = target_url
