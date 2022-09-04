from typing import Callable, Dict
from wsgiref.simple_server import make_server


def application(context: Dict, response_func: Callable):
    response_func('200 OK', [('Content-Type', 'text/html')])
    res_body = '<h1>Hello, %s!</h1>' % (context['PATH_INFO'][1:] or 'Web')
    return [res_body.encode('utf-8')]


if __name__ == '__main__':
    server = make_server('', 8000, application)
    print('Server Http On port 8000...')
    server.serve_forever()
