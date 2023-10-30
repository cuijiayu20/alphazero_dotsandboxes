import http.server
import json
import socketserver
import os

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        content_length = int(str(self.headers['Content-Length']))
        body = self.rfile.read(content_length)
        data = json.loads(body)
        with open("getstep.txt", "a")as f:
            f.write(data)
            f.flush()

# 设置 HTTP 服务器的 IP 和端口
host = 'localhost'
port = 8000

# 切换到指定的目录，开启 HTTP 服务器
web_dir = '../dotsandboxes'  # 指定目录
os.chdir(web_dir)
httpd = socketserver.TCPServer((host, port), MyRequestHandler)
print(f'Serving HTTP on http://{host}:{port} ...')
httpd.serve_forever()
