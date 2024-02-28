from zeep import Client
client = Client('http://localhost:8000')

result  = client.service.Saludar(nombre="Juan")
print(result)

result2 = client.service.Sumar(1,2)
print(result2)

result3 = client.service.CadenaPalindromo("all")
print(result3)