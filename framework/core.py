from urls import urlpatterns
import re

def not_found(environ, start_response):
    start_response('404 NOT FOUND', [('Content-Type', 'text/html;charset=utf-8')])
    response=['<h3>404 Not Found</h3>']
    return (line.encode() for line in response)

def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex , callback in urlpatterns:
        match = re.search(regex, path)
        if match:
            environ['args'] = match.group()
            return callback(environ, start_response)
    else:
        return not_found(environ, start_response)
