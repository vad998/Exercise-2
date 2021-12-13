from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()

        arr = ['a' * 10, 'b' * 11, 'c' * 12]
        
        for item in arr:
            self.wfile.write(b"%x\r\n%s\r\n" % (len(item), bytes(item, 'UTF-8')))

with HTTPServer(('', 8080), RequestHandler) as server: server.serve_forever()