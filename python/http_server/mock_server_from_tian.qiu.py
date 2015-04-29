#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os,cgi,time

PORT_NUMBER = 4052

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
		#time.sleep(10)
        self.send_response(200)
        self.send_header('Content-type','application/json;charset=utf-8')
        self.end_headers()

        if self.path=='/favicon.ico':
            return
                
        for line in open("mock-text-f"):
            self.wfile.write(line)

try:
#Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Started httpserver on port ' , PORT_NUMBER

        #Wait forever for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
                     
