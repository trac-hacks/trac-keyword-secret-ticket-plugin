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
    packages = find_packages(),
    entry_points = {
        'trac.plugins': [
            'kkbox = kkbox.trac.secretticket',
        ],
    },
)

