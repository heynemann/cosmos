#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from cosmos.cli.base_command import BaseCommand, BaseLister


class TargetAdd(BaseCommand):
    "Adds Cosmos API target."

    def get_parser(self, prog_name):
        parser = super(TargetAdd, self).get_parser(prog_name)
        parser.add_argument('name', help="The target name to be used in target-set.")
        parser.add_argument('url', help="The target URL for the desired Cosmos API.")
        return parser

    def take_action(self, parsed_args):
        name = parsed_args.name
        url = parsed_args.url
        self.credentials.target_add(name, url)
        self.credentials.save()

        self.say('Target %s added successfully.' % name)


class TargetList(BaseLister):
    def take_action(self, parsed_args):
        return (
            ('Name', 'URL', 'Reachable'),
            tuple(sorted(
                [
                    (name, url, self.credentials.validate_target(name, url) and 'yes' or 'no')
                    for name, url in self.credentials.targets.items()
                ]
            ))
        )
