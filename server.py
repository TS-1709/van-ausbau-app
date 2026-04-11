#!/usr/bin/env python3
"""Van Europa Roadtrip API — Tobi, Pauline, Noel, Raphael + Dachzelt."""
import json, os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

DATA = "/root/van-app/data.json"
CORS = {"Access-Control-Allow-Origin":"*","Access-Control-Allow-Methods":"GET,POST,OPTIONS","Access-Control-Allow-Headers":"Content-Type"}

def load():
    with open(DATA) as f: return json.load(f)
def save(d):
    with open(DATA,"w") as f: json.dump(d,f,ensure_ascii=False,indent=2)

class H(BaseHTTPRequestHandler):
    def _h(self,c=200,t="application/json"):
        self.send_response(c)
        for k,v in CORS.items(): self.send_header(k,v)
        self.send_header("Content-Type",t); self.end_headers()
    def do_OPTIONS(self): self._h(200)
    def do_GET(self):
        p=urlparse(self.path).path
        if p=="/":
            self._h(200,"text/html")
            with open("/root/van-app/index.html","rb") as f: self.wfile.write(f.read())
        elif p=="/api/data":
            self._h(); self.wfile.write(json.dumps(load(),ensure_ascii=False).encode())
        else: self._h(404)
    def do_POST(self):
        l=int(self.headers.get("Content-Length",0))
        body=json.loads(self.rfile.read(l))
        save(body); self._h(); self.wfile.write(b'{"ok":true}')
    def log_message(self,*a):pass

if __name__=="__main__":
    srv=HTTPServer(("0.0.0.0",8889),H)
    print("🚐 Europa Roadtrip on :8889"); srv.serve_forever()
