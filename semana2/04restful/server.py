from http.server import HTTPServer, BaseHTTPRequestHandler
import json


estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]



class RESTRequestHandler(BaseHTTPRequestHandler):
    def find_student(self,id,estudiantes):
        return next(
        (estudiante for estudiante in estudiantes if estudiante["id"] == id),
        None,
            )
    def data_reader(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
    def response_handler(self,status_code,data):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def do_GET(self):
        
        if self.path == "/estudiantes":
            self.response_handler(200,estudiantes)
            '''self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))'''
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id,estudiantes)
            if estudiante:
                self.response_handler(200,estudiante)
                '''self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))'''
    #-----------------------------------tarea----------------------------------
        elif self.path.startswith("/carreras"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            for estudiante in estudiantes:
                
                self.wfile.write(json.dumps(estudiante["carrera"]).encode("utf-8"))
        
        elif self.path.startswith("/estudiantes_Economia"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            for estudiante in estudiantes:
                if estudiante["carrera"] == "Economia":
                    self.wfile.write(json.dumps(estudiante).encode("utf-8"))
            
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
    
        

    def do_POST(self):
        if self.path == "/estudiantes":
            data=self.data_reader()
            data["id"] = len(estudiantes) + 1
            estudiantes.append(data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_PUT(self):
        if self.path.startswith("/estudiantes"):
            data = self.data_reader()
            id = data["id"]
            estudiante = self.find_student(id,estudiantes)
            if estudiante:
                estudiante.update(data)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_DELETE(self):
        if self.path == "/estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
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