from http.server import BaseHTTPRequestHandler
import urllib3

'''class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return'''
        
from os.path import dirname, abspath, join
dir = dirname(abspath(__file__))
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        with open(join(dir, '..', 'api', '01.Aficionado.w3u'), 'r') as file:
          for line in file:
            self.wfile.write(line.encode())
        return  
        
def inicia():
   target_url="https://raw.githubusercontent.com/rfontsv/python/main/api/01.Aficionado.w3u"
   http = urllib3.PoolManager()
   response = http.request('GET', target_url)
   data = response.data.decode('utf-8')
   
inicia()