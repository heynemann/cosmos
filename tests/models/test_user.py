#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from preggy import expect

from cosmos.models.user import User
from tests.base_test import ModelTestCase
from tests.fixtures.user import UserFactory


class UserModelTestCase(ModelTestCase):
    def test_can_create_user(self):
        user = UserFactory.create()

        retrieved = User.objects.filter(email=user.email).first()
        expect(retrieved).not_to_be_null()
        expect(retrieved.client_secret).to_equal(user.client_secret)

    def test_can_generate_secret(self):
        secret = User.generate_secret()
        expect(secret).not_to_be_null()
