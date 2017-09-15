from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse, json
from config import SERVER_PORT, SERVER_HOST

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        data = json.loads(post_body)

        self.wfile.write(data['foo'])
        return

if __name__ == '__main__':
    server = HTTPServer((SERVER_HOST, SERVER_PORT), GetHandler)
    print 'Starting server at http:/' + SERVER_HOST + ':8080'
    server.serve_forever()