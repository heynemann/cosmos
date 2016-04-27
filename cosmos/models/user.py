#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

import uuid

from redisco import models


class User(models.Model):
    email = models.Attribute(required=True)
    client_secret = models.Attribute(required=True)

    @classmethod
    def generate_secret(cls):
        return uuid.uuid4().hex
