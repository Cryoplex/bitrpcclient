#!/usr/bin/env python
# -*-coding: utf8 -*-


# Inspired by https://github.com/michaelliao/githubpy


import requests


__version__ = '0.0.1'


class BitRPCException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class BitRPCErrorResponse(BitRPCException):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return repr("%s code:%s; msg:%s" % (self.__class__,
                                            self.code,
                                            self.msg))


class _Callable(object):
    """Helper class to make the calls more intuitive."""
    def __init__(self, rpc_client, method):
        self.rpc_client = rpc_client
        self.method = method

    def __call__(self, *args, **kwargs):
        # Only to provide python 2 support.
        raw = kwargs.pop('raw', False)
        if kwargs:
            raise BitRPCException(
                    "Got an unexpected keyword argument '%s'" % kwags.keys())

        response = self.rpc_client._make_request(self.method, *args)
        if raw:
            return response
        if response.status_code == 200:
            result = response.json()['result']
            if result:
                return result
            else:
                err = response.json()['error']
                raise BitRPCErrorResponse(err['code'], err['message'])

        elif response.status_code == 404:
            raise BitRPCException(
                "Method not found")
        elif response.status_code == 500:
            error = response.json()['error']
            raise BitRPCErrorResponse(error['code'], error['message'])
        else:
            raise BitRPCException(
                    "Unexpected HTTP status_code: %d" % response.status_code)


class BitRPCClient(object):
    # Header to use in the requests
    HEADER = {'content-type': 'text/plain'}

    def __init__(self, user, password, addr="127.0.0.1", port=8332, url=None):
        """Initialize the rpc client

        user -- str with the user to connect with the rpc server
        password -- str with the password of user in the server
        addr -- str address of the server
        port -- int port to connect with. Default to JSON-RPC server of
                    bitcoind.(18332 default for testnet)
        url -- str instead of providing addr and port you could provide the
                   entire url
        """

        self.user = user
        self.password = password
        if url:
            self.url = url
        else:
            self.url = "http://%s:%s" % (addr, port)

    def __getattr__(self, attr):
        return _Callable(self, str(attr))

    def _make_request(self, method, *args):
        call_id = "bitrpcclient"
        if args:
            payload = {'method': method,
                       'params': [args],
                       'id': call_id}
        else:
            payload = {'method': method,
                       'id': call_id}

        response = requests.post(self.url,
                                 json=payload,
                                 headers=self.HEADER,
                                 auth=(self.user, self.password))
        return response
