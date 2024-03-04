import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# DELETE elimina todos los estudiantes por la ruta /estudiantes
ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", 
                                    url=ruta_eliminar)
print(eliminar_response.text)

# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica"
}

post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingenieria",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Luis",
    "apellido": "Lopez",
    "carrera": "Informatica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET busca a un estudiante por id /estudiantes/{id}
ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.request(method="GET", 
                                url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

# PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(put_response.text)
#----------------------------tarea 1-------------------------------------------
print("-----------------------------Las carreras de los estudiantes son:------------")
get_carreras = url + "carreras"
get_carreras_response = requests.request(
    method="GET", url=get_carreras
)
print(get_carreras_response.text)

#-----------------------añadiendo estudiantes de economia-------------------------
nuevo_estudiante = {
    "nombre": "Abel",
    "apellido": "Savedra",
    "carrera": "Economia",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)

nuevo_estudiante = {
    "nombre": "Jorge",
    "apellido": "Quiroga",
    "carrera": "Economia",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)



print("----------------------Los estudiantes de economia son:-----------------------")
get_Economia = url + "estudiantes_Economia"
get_carreras_response = requests.request(
    method="GET", url=get_Economia
)

print(get_carreras_response.text)