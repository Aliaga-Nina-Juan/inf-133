import requests

#URL del servidor Flask
url = 'http://localhost:5000/'

#Realizar una solicitud GET al servidor Flask
response = requests.get(url)

#Verifica si la solicitud fue exitosa (codigo de estado 200)ç
if response.status_code == 200:
    print("Respuesta del servidor")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)
    
#Metodo GET: Obtener un saludo proporcioando el nombre como parametro en la url

params = {'nombre':'tu_nombre'}
response = requests.get(url+'saludar',params=params)

#Verificar si la solicitud GET fue exitosa
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor GET:", mensaje)
else:
    print("Error al conectar con el servidor (GET): ",response.status_code)
    
params = {
    'num1':2,
    'num2':3
}
response = requests.get(url+'sumar',params=params)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor GET:",mensaje)
    
params = {'palindromo':'opp'}
response = requests.get(url+'palindromo',params=params)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor GET: ",mensaje)
    
params = {
    'cadena':'peeeersonal',
    'vocal':'e'
}
response = requests.get(url+'contar_vocales',params=params)
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor GET: ",mensaje)