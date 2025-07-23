
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # HTTP 상태 코드랑 해더 전송
        self.send_response(200) # 200은 통신에서 연결이 잘 됐다는거 의미
        self.send_header("Content-type", "test/html") 
        self.end_headers()

        # 실제로 서버에서 응답 받을 메시지
        self.wfile.write(b"<h1>Hello, world! (from pure HTTP)</h1>")

server_address = ("", 8000) # 내 주소로 8000번 라우팅을 하겠다!
# 127.0,0,1:8000 or localhost:8000

http_server = HTTPServer(server_address, SimpleHandler)
print("[basic_http_server] http://localhost:8000")

http_server.serve_forever()