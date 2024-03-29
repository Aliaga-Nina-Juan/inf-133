import requests

#definir la consulta grapql
query = """
    {
        estudiantePorCarrera(carrera:"Arquitectura"){
            nombre
        }
    }
"""
url = 'http://localhost:8000/graphql'

response = requests.post(url , json={'query':query})
print(response.text)