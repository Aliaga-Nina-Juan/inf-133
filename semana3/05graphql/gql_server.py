from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation



class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()
    
estudiantes = {
    Estudiante(
        id = 1,
        nombre = "Juan",
        apellido = "Aliaga",
        carrera = "Arquitectura",
    ),
    Estudiante(
        id = 2,
        nombre = "Ronald",
        apellido = "Gary",
        carrera = "Arquitectura",
    )
}

class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiante_por_id = Field(Estudiante , id =Int())
    estudiante_por_nombre_apellido = Field(Estudiante, nombre=String(),apellido=String())
    estudiante_por_carrera = Field(Estudiante, carrera =String())
    
    def resolve_estudiantes(root, info):
        print(estudiantes)
        return estudiantes
    def resolve_estudiante_por_id(root, info,id):
        for estudiante in estudiantes:
            if estudiante.id == id:
                return estudiante
        return None
    def resolve_estudiante_por_nombre_apellido(root, info,nombre,apellido):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre:
                if estudiante.apellido == apellido:
                    return estudiante
        return None    
    def resolve_estudiante_por_carrera(root, info,carrera):
        for estudiante in estudiantes:
            if estudiante.carrera == carrera:
                return estudiante
        return None              
schema = Schema(query=Query)    
class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self , status , data):
        self.send_response(status)
        self.send_header("Content-type","aplication/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})
            
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()