#!/usr/bin/env python
#
# Copyright (C) 2012-2013 KKBOX Technologies Limited
# Copyright (C) 2012-2013 Gasol Wu <gasol.wu@gmail.com>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import find_packages, setup

PACKAGE = 'TracKeywordSecretTicketsPlugin'
VERSION = '1.0.2'

try:
    import trac
    if trac.__version__ < '0.11.6':
        print "%s %s requires Trac >= 0.11.6" % (PACKAGE, VERSION)
        sys.exit(1)
except ImportError:
    pass

setup(
    name = PACKAGE,
    version = VERSION,
    author = 'Gasol Wu',
    author_email = 'gasolwu@kkbox.com',
    description = 'Adds ticket security policy based on keyword or group',
    license = '3-Clause BSD',
    keywords = 'permission permissions acl trac keywords plugin',
    packages = find_packages(),
    entry_points = {
        'trac.plugins': [
            'keywordsecretticket = keywordsecretticket.policy',
        ],
    },
)

