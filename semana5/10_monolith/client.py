import requests
url = "http://localhost:8000"


response = requests.get(f"{url}/post/1")

nueva_publicación = {
    3: {
        "title": "Mi segunda publicacion",
        "content": "¡Hola mundo! Esta es mi primera publicación en el blog.",
    }
}

ruta_post = url + "/posts"

post_response = requests.post(url=ruta_post, json=nueva_publicación)
print(post_response.text)

response = requests.post(f"{url}/post/1")
print(response.text)