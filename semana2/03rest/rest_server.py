from http.server import HTTPServer, BaseHTTPRequestHandler
import json

#esto es una lista por los corchetes 
#lo que esta dentro de las llaves es un diccionario
estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    #funcion obtener dato
    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/eliminar_estudiante":
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path.startswith("/buscar_estudiante_id/"):
            id = int(self.path.split("/")[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            
            if estudiante:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))
                #error de 404 error del cliente
    #--------------------------------------TAREA-----------------------------------------------------
        elif self.path.startswith("/buscar_nombre/"):
            car = "P"
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["nombre"][0] == car),
                None,
            )
            
            if estudiante:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante["nombre"]).encode("utf-8"))
    #----------------------------------------ejercicio2-----------------------------------------------             
        elif self.path.startswith("/contar_carreras/"):
            car = str(self.path)
            con = 0
            for estudiante in estudiantes:
                if "/contar_carreras/"+estudiante["carrera"] == car:
                    con=con+1
            con = json.loads(con.decode("utf-8"))
            self.wfile.write(json.dumps(con).encode("utf-8"))           
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    #funcion publicar
    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            #convierte texto plano a json
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            #agrega post_data a la lista estudiantes
            estudiantes.append(post_data)
            self.send_response(201)
            #se ha realizado modificacion
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/actualizar_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            id = post_data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(post_data)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()