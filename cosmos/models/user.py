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
    client_id = models.Attribute(required=True)
    client_secret = models.Attribute(required=True)

    def generate_secret(self):
        self.client_secret = uuid.uuid4().hex
