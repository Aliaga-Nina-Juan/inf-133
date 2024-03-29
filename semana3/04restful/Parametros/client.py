import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
#print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
#print(post_response.text)

ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Ronald",
    "apellido": "Aliaga",
    "carrera": "Quimica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)

# GET filtrando por nombre con query params
ruta_get = url + "estudiantes?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print("El nombre buscado es: ")
print(get_response.text)
#GET filtrando por apellido con query params
ruta_get_apellido = url + "estudiantes?apellido=Perez"
get_response_apellido = requests.request(method="GET", url=ruta_get_apellido)
print("El apellido buscado es:")
print(get_response_apellido.text)

