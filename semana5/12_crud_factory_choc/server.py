from http.server import HTTPServer, BaseHTTPRequestHandler
import json

chocolates = {}

class variedadChocolates:
    def __init__(self, tipo_chocolate, peso, sabor , relleno=None):
        self.tipo_chocolate = tipo_chocolate
        self.peso = peso
        self.sabor = sabor
        self.relleno = relleno

class Tableta(variedadChocolates):
    def __init__(self, peso,sabor):
        super().__init__("Tableta", peso,sabor)

        
class Bombon(variedadChocolates):
    def __init__(self, peso,sabor,relleno):
        super().__init__("Bombon", peso,sabor,relleno)
class Trufa(variedadChocolates):
    def __init__(self, peso,sabor,relleno):
        super().__init__("Trufa", peso,sabor,relleno)

        
class fabricaChocolates:
    @staticmethod
    def create_chocolate(tipo_chocolate,peso,sabor,relleno=None):
        if tipo_chocolate == "Tableta":
            return Tableta(peso,sabor)
        elif tipo_chocolate == "Bombon":
            return Bombon(peso,sabor,relleno)
        elif tipo_chocolate == "Trufa":
            return Bombon(peso,sabor,relleno)
        else:
            raise ValueError("Tipo de chocolate ingresado no válido")
        
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler,status,data):
        handler.send_response(status)
        handler.send_header("Content-type","application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))
    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))
    
class ChocolateService:
    def __init__(self):
        self.factory = fabricaChocolates()
