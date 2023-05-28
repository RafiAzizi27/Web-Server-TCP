from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from urllib.parse import parse_qs

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
#fungsi do_POST menerima inputan dari name dan email
    def do_POST(self):                                              
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode('utf-8'))

        name = data.get('name', [''])[0]
        email = data.get('email', [''])[0]

        print(f"Received data: name={name}, email={email}")

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(f"Received data: name={name}, email={email}".encode('utf-8')) 

#menampilkan halaman index dan mengirim 404 jika halaman tidak ditemukan akan muncul error
    def do_GET(self):
        if self.path != '/':
            self.send_error(HTTPStatus.NOT_FOUND, '404 Not Found')
            return

        with open('index.html', 'rb') as file:
            content = file.read()

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(content)

#opsi sebagai mendefinisikan konfigurasi permintaan pada server dengan metode CORS
    def do_OPTIONS(self):
        self.send_response(HTTPStatus.NO_CONTENT)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.end_headers()

#binding port dan host
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
print("Starting server on http://localhost:8000")

#start server dan akan mati jika dimatikan secara manual
httpd.serve_forever()
