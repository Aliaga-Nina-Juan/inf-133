# Importamos la biblioteca requests para hacer peticiones HTTP
import requests

# Definimos la URL del servicio al que vamos a hacer la petición
url = "http://localhost:8000/delivery"

# Definimos los encabezados HTTP que vamos a enviar con la petición
headers = {"Content-Type": "application/json"}

# Definimos el tipo de vehículo como "motocycle"
vehicle_type = "motorcycle"
data = {"vehicle_type": vehicle_type}

# Hacemos una petición POST a la URL con los datos y encabezados definidos
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling delivery:", response.text)

#----------------vehiculo 2----------------------------
vehicle_type = "drone"
data1 = {"vehicle_type": vehicle_type}

response1 = requests.post(url, json=data1, headers=headers)

if response1.status_code == 200:
    print(response1.text)
else:
    print("Error scheduling delivery:", response.text)
#-------------vehiculo 3 -------------------------
vehicle_type = "scout"
data2 = {"vehicle_type": vehicle_type}

response2 = requests.post(url, json=data2, headers=headers)

if response2.status_code == 200:
    print(response2.text)
else:
    print("Error scheduling delivery:", response.text)
