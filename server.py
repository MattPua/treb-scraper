from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse, json
from config import SERVER_PORT, SERVER_HOST
from bs4 import BeautifulSoup
from script import parse_listing

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

        soup = BeautifulSoup(post_body, 'html.parser')
        link = soup.table.find('a')
        link_url = link.attrs['href']
        parse_listing(link_url)
        return

if __name__ == '__main__':
    server = HTTPServer((SERVER_HOST, SERVER_PORT), GetHandler)
    print 'Starting server at http://' + SERVER_HOST + ':8080'
    server.serve_forever()