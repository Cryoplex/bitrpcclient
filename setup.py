#!/usr/bin/env python

from distutils.core import setup

import bitrpcclient

kw = dict(
    name = 'bitrpcclient',
    version = bitrpcclient.__version__,
    description = 'JSON-RPC small client for bitcoind',
    author = 'Francisco Montoto',
    author_email = 'fmontoto@gmail.com',
    url = 'https://github.com/fmontoto/bitrpcclient',
    download_url = 'https://github.com/fmontoto/bitrpcclient/',
    py_modules = ['bitrpcclient']
)

setup(**kw)
