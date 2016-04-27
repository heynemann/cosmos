#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

import factory

from cosmos.models.user import User
from tests.fixtures.base_fixture import BaseFactory


class UserFactory(BaseFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    client_secret = factory.Faker('uuid4')
