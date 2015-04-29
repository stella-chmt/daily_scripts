#encoding=utf-8
'''
Created on 2012-11-7

@author: Steven
http://www.lifeba.org
基于BaseHTTPServer的http server实现，包括get，post方法，get参数接收，post参数接收。
'''
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import io,shutil  
import urllib,time
import getopt,string
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.process(2)

    def do_POST(self):
        self.process(1)
        
    def process(self,type):
        
        content =""
        if type==1:#post方法，接收post参数
            datas = self.rfile.read(int(self.headers['content-length']))
            datas = urllib.unquote(datas).decode("utf-8", 'ignore')#指定编码方式
            datas = transDicts(datas)#将参数转换为字典
            if datas.has_key('data'):
                content = "data:"+datas['data']+"\r\n"
                
        if '?' in self.path:
            query = urllib.splitquery(self.path)
            action = query[0] 
                     
            if query[1]:#接收get参数
                queryParams = {}
                for qp in query[1].split('&'):
                    kv = qp.split('=')
                    queryParams[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
                    #content+= kv[0]+':'+queryParams[kv[0]]+"\r\n"
                    data = {"otherinfo":{"bizip":"192.168.7.101:4013","debuginfo":{"pigeon_search":{"processorinfo":"original:,splitwords:null"}},"engineip":"192.168.7.101","enginetime":"46","executiontime":"149","scorecontext":"","searchinfo":""},"records":[{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"1","int16":"1","int32":"1","int64":"1","int8":"100","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"浦东机场","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"浦东机场"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"2","int16":"1","int32":"1","int64":"1","int8":"101","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"浦东国际机场","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"浦东国际机场"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"3","int16":"1","int32":"1","int64":"1","int8":"104","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"串串香","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"串串香"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"4","int16":"1","int32":"1","int64":"1","int8":"105","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"早餐","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"早餐"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"5","int16":"1","int32":"1","int64":"1","int8":"108","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"中国银行","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"中国银行"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"6","int16":"1","int32":"1","int64":"1","int8":"109","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"京东","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"京东"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"121.393721:31.193921","id_":"7","int16":"1","int32":"1","int64":"1","int8":"1","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"121.393721:31.193921 121.403721:31.193921","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"集成测试","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"集成测试"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"8","int16":"1","int32":"1","int64":"1","int8":"103","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"冷锅串串","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"冷锅串串"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"9","int16":"1","int32":"1","int64":"1","int8":"106","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"早茶","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"早茶"},{"attributes":"a:1 b:c","float32":"1.0","float64":"1.0","geo":"120.0:30.0","id_":"10","int16":"1","int32":"1","int64":"1","int8":"111","int8_s":"1","multi_float32":"1.0 2.0","multi_float64":"1.0 2.0","multi_geo":"120.0:30.0 130.0:40.0","multi_int32":"1 2","multi_int64":"1 2","multi_property":"1:2 3:4","multi_string":"abc def","multi_utf16string":"abc def","polygon_area":"121.541769:31.256864 121.535977:31.25602 121.530949:31.255049,121.506992:31.254381 121.506064:31.256434 121.504777:31.25791;121.556966:31.268401 121.556966:31.268401;121.506992:31.254381","property":"1:2","string":"abc","text":"冷锅串串香","time":"2014-09-22 00:00:00.0","utf16string":"abc","utf16text":"冷锅串串香"}],"statistics":{},"status":"OK","totaldocs":44,"totalhits":17}
                    #print "DATA:",data
                    #data = {'a':"A",'b':(2,4),'c':3.0}                   
                    content = json.dumps(data)
                    #print "JSON:",content
                    #content=u"{otherinfo: {bizip: \"192.168.7.101:4013\",debuginfo:OK}"

            #指定返回编码
            enc="utf-8"  
            content = content.encode(enc)          
            f = io.BytesIO()  
            f.write(content)  
            f.seek(0)  
            self.send_response(200)  
            self.send_header("Content-type", "text/html; charset=%s" % enc)  
            self.send_header("Content-Length", str(len(content)))  
            self.end_headers()  
            shutil.copyfileobj(f,self.wfile)   

def transDicts(params):
    dicts={}
    if len(params)==0:
        return
    params = params.split('&')
    for param in params:
        dicts[param.split('=')[0]]=param.split('=')[1]
    return dicts
       
if __name__=='__main__':
    
    try:
        server = HTTPServer(('', 8000), MyRequestHandler)
        print 'started httpserver...'
        server.serve_forever()

    except KeyboardInterrupt:
        server.socket.close()
    
    pass
