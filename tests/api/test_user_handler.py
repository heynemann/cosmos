#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from json import loads

from preggy import expect

from tests.base_test import TornadoTestCase
from tests.fixtures.user import UserFactory
from cosmos.models.user import User


class RegisterHandlerTestCase(TornadoTestCase):
    def test_cant_register_new_user_without_email(self):
        response = self.post('/user/register')
        expect(response.code).to_equal(400)

    def test_cant_register_new_user_with_existing_email(self):
        user = UserFactory.create()

        response = self.post('/user/register', None, "email=%s" % user.email)
        expect(response.code).to_equal(409)

    def test_can_register_new_user(self):
        response = self.post('/user/register', None, "email=%s@gmail.com" % User.generate_secret())
        expect(response.code).to_equal(200)

        obj = loads(response.body)
        expect(obj).to_include('email')
        expect(obj).to_include('clientSecret')

        retrieved = User.objects.filter(email=obj['email']).first()
        expect(retrieved).not_to_be_null()
        expect(retrieved.client_secret).to_equal(obj['clientSecret'])
