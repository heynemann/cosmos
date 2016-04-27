#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from json import loads

from cosmos.cli.base_command import BaseCommand


class Register(BaseCommand):
    "Registers a new user."

    def get_parser(self, prog_name):
        parser = super(Register, self).get_parser(prog_name)
        parser.add_argument('--email', required=True, help="The email address for the user being registered.")
        return parser

    def take_action(self, parsed_args):
        email = parsed_args.email
        status, result = self.post("/user/register", email=email)

        if status == 200:
            obj = loads(result)
            self.app.stdout.write(
                'User registered successfully with email "%s" and client-secret "%s".\n\n'
                'Please write down this values in order to log-in to cosmos in the future.\n\n' % (
                    obj['email'], obj['clientSecret']
                )
            )
            return

        if status == 409:
            self.app.stdout.write(
                'Could not register user %s. There is an user registered with this email already.\n'
                'Did you forget the client-secret? Please use "cosmos remind-secret" if that\'s the case.\n\n' % (
                    email
                )
            )
