About
=====

A minimal [TiddlyWeb](https://github.com/tiddlyweb/tiddlyweb) plugin 
that can act as a kick-starter to plugin development, testing, packaging 
and distribution.

Requirements
============

* [Python](http://www.python.org/)
* make
* A working TiddlyWeb instance to test against
* [py.test](http://pytest.org/latest/) to run the tests.

Modifying
=========

`setup.py` is used to package up the plugin, install and distribute.
You should edit this as required.

Change the plugin name in `tiddlywebplugin.py` to what it needs to be.
The convention used is tiddlywebplugins.name

Plugin code lives in the `tiddlywebplugins` directory.

Tests live in the `test` directory.

Usage
=====

`make test` runs the tests.  Currently there is just the one that 
ensures the plugin can be imported.

`make install` installs the plugin as a package on your system 
(you may need sudo for this.)
You can then reference the plugin from your TiddlyWeb configuration 
as a system plugin e.g:

`system_plugins': ['tiddlywebplugins.hello_world']`

`make release` packages and uploads the plugin to [PyPI](http://pypi.python.org/pypi) for distribution.  I've yet to test this out.

Notes
=====

If you wish to develop a plugin for [Tiddlypace](https://github.com/TiddlySpace/tiddlyspace) 
make sure you declare the plugin in the configuration file _before_ the
tiddlywebplugins.tiddlyspace plugin e.g:

`'system_plugins': ['tiddlywebplugins.my_plugin', 'tiddlywebplugins.tiddlyspace']`

Further Reading
===============

The creator of TiddlyWeb, @cdent, has a [plugin tutorial](http://tiddlyweb.peermore.com/wiki/bags/docs/tiddlers/Plugin%20Tutorial)
you can follow.

Todo
====

* Write an example test.
* Test PyPI upload.
* Further explanation of the plugin structure and files involved.
