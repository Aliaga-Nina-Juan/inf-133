import requests

# Definir la consulta GraphQL
#tres cadenas para cadena de varias lineas
query = """
    {
        hello
        goodbye
    }
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)
