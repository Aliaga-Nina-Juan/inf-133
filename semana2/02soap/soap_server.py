from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler


dispatcher = SoapDispatcher(
    "Ejemplo-de-server",
    location = "http://localhost:8000/",
    action="http://localhost:8000/",
    namespace= "http://localhost:8000/",
    trace=True,
    ns=True,
)

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns = {"saludo":str},
    args = {"nombre":str},
)
#Tarea
def SumaDosNumeros(x,y):
    return "La Suma es, {}!".format(x+y)

dispatcher.register_function(
    "Sumar",
    SumaDosNumeros,
    returns = {"Suma":int},
    args = {"x":int,"y":int},
)

def CadenaPalindromo(z):
    if str(z) == str(z)[::-1]:
        return True
    else:
        return False
    
dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns = {"Boolean":bool},
    args = {"z":str},
)



server = HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()