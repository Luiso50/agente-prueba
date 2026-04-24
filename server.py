#!/usr/bin/env python3
"""
Servidor HTTP simple para el Agente BM Cargo
Ejecuta: python server.py
Luego abre: http://localhost:8000
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers para evitar problemas de CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        # Servir archivos estáticos
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    # Cambiar al directorio del servidor
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor iniciado en http://localhost:{PORT}")
        print(f"📁 Sirviendo archivos desde: {os.getcwd()}")
        print(f"⏹️  Presiona Ctrl+C para detener")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n❌ Servidor detenido")
