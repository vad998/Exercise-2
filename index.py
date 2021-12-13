from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.send_header("Transfer-Encoding", "chunked")
        self.end_headers()

        chunks = ['a' * 10, 'b' * 11, 'c' * 12]
        
        for chunkItem in chunks:
            self.wfile.write(b"%x\r\n%s\r\n" % (len(chunkItem), bytes(chunkItem, 'UTF-8')))

with HTTPServer(('', 8080), RequestHandler) as server: server.serve_forever()