#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cosmos.
# https://github.com/heynemann/cosmos

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Bernardo Heynemann <heynemann@gmail.com>

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import requests
from webbrowser import open_new

from cosmos.cli.base_command import BaseCommand

REDIRECT_URL = 'http://localhost:2458/'


def get_access_token_from_url(url):
    """
    Parse the access token from Facebook's response
    Args:
        uri: the facebook graph api oauth URI containing valid client_id,
             redirect_uri, client_secret, and auth_code arguements
    Returns:
        a string containing the access key
    """
    response = requests.get(url)
    token = response.text
    return token.split('=')[1].split('&')[0]


class HTTPServerHandler(BaseHTTPRequestHandler):

    """
    HTTP Server callbacks to handle Facebook OAuth redirects
    """
    def __init__(self, request, address, server, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        BaseHTTPRequestHandler.__init__(self, request, address, server)

    def log_message(self, format, *args):
        return

    def do_GET(self):
        GRAPH_API_AUTH_URI = (
            'https://graph.facebook.com/v2.2/oauth/'
            'access_token?client_id=%s&redirect_uri=%s'
            '&client_secret=%s&code=' % (
                self.client_id,
                REDIRECT_URL,
                self.client_secret,
            )
        )

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if 'code' in self.path:
            self.auth_code = self.path.split('=')[1]

            # Display to the user that they no longer need the browser window
            self.wfile.write(
                '<html><h1>You may now close this window.'
                '</h1></html>'
            )

            self.server.access_token = get_access_token_from_url(
                    GRAPH_API_AUTH_URI + self.auth_code)


class TokenHandler:
    """
    Class used to handle Facebook oAuth
    """
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_access_token(self):
        """
         Fetches the access key using an HTTP server to handle oAuth
         requests
            Args:
                appId:      The Facebook assigned App ID
                appSecret:  The Facebook assigned App Secret
        """

        ACCESS_URI = (
            'https://www.facebook.com/dialog/'
            'oauth?client_id=%s&redirect_uri=%s'
            '&scope=ads_management' % (
                self.client_id,
                REDIRECT_URL
            )
        )

        open_new(ACCESS_URI)
        httpServer = HTTPServer(
                ('localhost', 2458),
                lambda request, address, server: HTTPServerHandler(
                    request, address, server, self.client_id, self.client_secret)
                )

        # This function will block until it receives a request
        httpServer.handle_request()

        # Return the access token
        return httpServer.access_token


# https://www.pmg.com/blog/logging-facebook-oauth2-via-command-line-using-python/
class Login(BaseCommand):
    "Logs into Cosmos."

    def get_parser(self, prog_name):
        parser = super(Login, self).get_parser(prog_name)
        # parser.add_argument('--email', required=True, help="The email address for the user being authenticated.")
        return parser

    def take_action(self, parsed_args):
        handler = TokenHandler(client_id='1751269921758147', client_secret='6b17ce1a4f5ceaf110f12ad3063e3360')
        token = handler.get_access_token()

        self.credentials.authenticate(token)
        self.validate_user()
        self.credentials.save()

        self.say('User %s authenticated successfully.' % self.credentials.name)
