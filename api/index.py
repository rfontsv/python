from http.server import BaseHTTPRequestHandler
import urllib3

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        '''self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))'''
        target_url="https://raw.githubusercontent.com/rfontsv/python/main/api/01.Aficionado.w3u"
        http = urllib3.PoolManager()
        response = http.request('GET', target_url)
        data = response.data.decode('utf-8')
        return
