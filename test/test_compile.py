def test_compile():
	try:
		import tiddlywebplugins.hello_world
		assert True
	except ImportError, exc:
		assert False, exc
