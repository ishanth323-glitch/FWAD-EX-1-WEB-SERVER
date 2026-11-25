from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    pass

server = HTTPServer(('127.0.0.1', 8000), CustomHandler)

print("Server started at http://127.0.0.1:8000")

server.serve_forever()