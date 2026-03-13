import json
from http.server import BaseHTTPRequestHandler, HTTPServer

agents = []

class DiscoveryHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/agents":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(agents).encode())

    def do_POST(self):
        if self.path == "/register":
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            agent = json.loads(data)

            agents.append(agent)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Agent registered")

def run():
    server = HTTPServer(("0.0.0.0", 8000), DiscoveryHandler)
    print("AI Civilization Discovery Server Running on port 8000")
    server.serve_forever()

if __name__ == "__main__":
    run()
