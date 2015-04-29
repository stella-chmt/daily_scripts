# -*- coding:utf-8 -*-
import sys  
import BaseHTTPServer  
import urllib
from SimpleHTTPServer import SimpleHTTPRequestHandler  
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from sys import version as python_version
from cgi import parse_header, parse_multipart

if python_version.startswith('3'):
    from urllib.parse import parse_qs
else:
    from urlparse import parse_qs

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print "get请求"
        self.send_response(200)
 
    def do_POST(self):
        print "post请求"
        self.send_response(200)
        print self.headers

        #这种方式得到的postvars是post数据的dict,而不是一系列url
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(
                    self.rfile.read(length),
                    keep_blank_values=1)
        else:
            postvars = {}
        print postvars

        '''
        #这种方式得到的是url样式的post数据
        datas = self.rfile.read(int(self.headers['content-length']))
        #datas = urllib.unquote(datas).decode("utf-8", 'ignore')
        datas = urllib.unquote(datas)
        print datas
        '''

try:
#Create a web server and define the handler to manage the
        #incoming request
	PORT_NUMBER = 8888
        server = HTTPServer(('', PORT_NUMBER), MyRequestHandler)
        print 'Started httpserver on port ' , PORT_NUMBER

        #Wait forever for incoming http requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
