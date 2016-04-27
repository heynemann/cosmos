#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from json import dumps

from cosmos.api.handlers import BaseHandler
from cosmos.models.user import User


class RegisterHandler(BaseHandler):
    def post(self):
        email = self.get_argument('email')
        user = User(email=email, client_secret=User.generate_secret())
        user.save()

        self.write(dumps({
            "email": email,
            "clientSecret": user.client_secret
        }))
