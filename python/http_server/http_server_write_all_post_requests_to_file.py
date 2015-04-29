# -*- coding:utf-8 -*-

import urllib
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print "get请求"
        self.send_response(200)

    def do_POST(self):
        print "post请求"
        self.send_response(200)
        datas = self.rfile.read(int(self.headers['content-length']))
        #datas = urllib.unquote(datas).decode("utf-8", 'ignore')
        datas = urllib.unquote(datas)

        #存储log到yyyy-m-dd.log文件
        file_name = self.get_date_string()
        path_name = '%s/%s.log' % ("./",file_name)
        fwrite = open(path_name,'a')
        fwrite.write("%s\n" % datas)
        fwrite.close()

    #获取当前时间yyyy-m-dd，例如2015-4-21
    def get_date_string(self):
        now = time.time()
        clock_now = time.localtime(now)
        cur_time = list(clock_now)
        date_string = "%d-%d-%d" % (cur_time[0], cur_time[1], cur_time[2])
        return date_string

try:
#Create a web server and define the handler to manage the incoming request
    PORT_NUMBER = 8888
    server = HTTPServer(('', PORT_NUMBER), MyRequestHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()

