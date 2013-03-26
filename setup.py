#
# Copyright (C) 2012-2013 KKBOX Technologies Limited
# Copyright (C) 2012-2013 Gasol Wu <gasol.wu@gmail.com>
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import find_packages, setup

try:
    import trac
    if trac.__version__ < '0.11.6':
        print "KKBOXTracPlugin %s requires Trac >= 0.11.6" % version
        sys.exit(1)
except ImportError:
    pass

setup(
    name = 'KKBOXTracPlugin',
    version = '1.0.1',
    author = 'Gasol Wu',
    author_email = 'gasolwu@kkbox.com',
    description = 'Adds ticket security policy based on keyword or group',
    license = '3-Clause BSD',
    packages = find_packages(),
    entry_points = {
        'trac.plugins': [
            'kkbox = kkbox.trac.secretticket',
        ],
    },
)

