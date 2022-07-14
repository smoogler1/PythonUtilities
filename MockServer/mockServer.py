
from http.server import BaseHTTPRequestHandler, HTTPServer
from dict import responses_dict
from termcolor import colored
import os
os.system('color')

ip = '10.254.240.3'
serverPort = 8082

def process_request(http_handler):
    body = ''
    url = ''
        
    for key in responses_dict:
        if(key == http_handler.path):
            body = responses_dict[key]
            url = key
                
    http_handler.send_response(200)
    http_handler.send_header('Content-type','application/json')
    http_handler.send_header("Content-Length", len(body))
    http_handler.send_header("Connection", "close")
    http_handler.end_headers()

    content_len = int(http_handler.headers.get('Content-Length'))
    if content_len:
        print(colored("******* REQUEST BODY **************",'yellow'));
        print(colored(http_handler.rfile.read(content_len).decode("utf-8"),'yellow'))
        print(colored("************************************",'yellow'));

    
    print(colored("******* RESPONSE BODY **************",'green'));
    print(colored(body,'green'))
    print(colored("************************************",'green'));
    
    http_handler.wfile.write(bytes(body,'utf-8'))

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        process_request(self)

    def do_POST(self):
        process_request(self)


def run(server_class=HTTPServer, handler_class=handler, port=serverPort):
    server_address = (ip, port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running at {ip}:{serverPort}...')
    httpd.serve_forever()

run()
