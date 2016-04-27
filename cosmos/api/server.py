#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>


import argparse
import sys

import tornado.ioloop
from tornado.httpserver import HTTPServer
import redisco

from cosmos.api.app import CosmosApp
from cosmos import logger


def get_application():
    return CosmosApp()


def run_server(application, port, ip):
    server = HTTPServer(application)

    server.bind(port, ip)

    server.start(1)


def main(arguments=None):
    '''Runs thumbor server with the specified arguments.'''
    if arguments is None:
        arguments = sys.argv[1:]

    parser = argparse.ArgumentParser(prog='cosmos-api')
    parser.add_argument('--port', default=8888, type=int, help="Port to bind cosmos-api to.")
    parser.add_argument('--ip', default="0.0.0.0", help="IP Address to bind cosmos-api to.")
    options = parser.parse_args(arguments)

    application = get_application()
    run_server(application, options.port, options.ip)

    redisco.connection_setup(host='localhost', port=4444, db=1)

    try:
        logger.debug('cosmos-api running at %s:%d' % (options.ip, options.port))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.stdout.write("-- cosmos-api closed by user interruption --\n")

if __name__ == "__main__":
    main(sys.argv)
