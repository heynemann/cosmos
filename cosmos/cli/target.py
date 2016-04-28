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

        self.say('\nTarget %s added successfully.' % name)


class TargetRemove(BaseCommand):
    "Removes Cosmos API target."

    def get_parser(self, prog_name):
        parser = super(TargetRemove, self).get_parser(prog_name)
        parser.add_argument('name', help="The target name to be removed.")
        return parser

    def take_action(self, parsed_args):
        name = parsed_args.name
        self.credentials.target_remove(name)
        self.credentials.save()

        self.say('Target %s removed successfully.' % name)


class TargetSet(BaseCommand):
    "Sets the specified target as the current Cosmos target."

    def get_parser(self, prog_name):
        parser = super(TargetSet, self).get_parser(prog_name)
        parser.add_argument('name', help="The target name to be removed.")
        return parser

    def take_action(self, parsed_args):
        name = parsed_args.name
        self.credentials.target_set(name)
        self.credentials.save()

        self.say('Target %s set successfully.' % name)


class TargetList(BaseLister):
    "Lists all available Cosmos API targets."
    def prefix(self):
        self.say('{t.green}List of available targets:{t.normal}'.format(t=self.color))

    def take_action(self, parsed_args):
        return (
            ('Name', 'URL', 'Reachable'),
            tuple(sorted(
                [
                    (
                        "%s%s" % (name, name == self.credentials.current_target and " *" or ""),
                        url,
                        self.credentials.validate_target(name, url, False) and 'yes' or 'no'
                    )
                    for name, url in self.credentials.targets.items()
                ]
            ))
        )

    def suffix(self):
        self.say('{t.bold}* currently selected target{t.normal}'.format(t=self.color))
