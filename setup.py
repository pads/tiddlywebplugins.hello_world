import os
from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
	namespace_packages = ['tiddlywebplugins'],
	name = 'tiddlywebplugins.hello_world',
	version = VERSION,
	description = 'A minimal TiddlyWeb plugin that can act as a kick-starter to plugin development, testing, packaging and distribution.',
	long_description=file(os.path.join(os.path.dirname(__file__), 'README')).read(),
	author = 'Ben Paddock',
	url = 'http://pypi.python.org/pypi/tiddlywebplugins.hello_world',
	packages = find_packages(exclude=['test']),
	author_email = 'pads@thisispads.me.uk',
	platforms = 'Posix; MacOS X; Windows',
	install_requires = ['tiddlyweb'],
	zip_safe = False,
	)
