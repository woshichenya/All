#!/usr/bin/python
# -*- coding: UTF-8 -*-
def yingyong(environ, start_response):

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>hello man!</h1>']

from wsgiref.simple_server import make_server

a=900
httpd=make_server('10.131.98.195',900,yingyong)
httpd.serve_forever()
