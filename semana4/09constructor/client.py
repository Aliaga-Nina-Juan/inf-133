import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

mi_pizza = {
    "tamaño": "Grande",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso"]
}
mi_pizza2 = {
    "tamaño": "Grande",
    "masa": "Gruesa",
    "toppings": ["Peña", "Queso"]
}

response = requests.post(url, json=mi_pizza2, headers=headers)
print(response.json())

