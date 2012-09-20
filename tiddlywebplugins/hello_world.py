def hello(environ, start_response):
	start_response('200', [])
	return ['<html><body><h1>hello, world!</h1></body></html>']

def init(config):
	config['selector'].add('/hello', GET=hello)
