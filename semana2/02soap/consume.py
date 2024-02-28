#1 pip install virtualenv si sale error Set-ExecutionPolicy Unrestricted -Scope Process
#2  python -m virtualenv venv
#3  .\venv\Scripts\activate
#4  pip list    .....version de pip
#5  Instalando el cliente en el ENV ...pip install zeep
#6  Importando el cliente... from zeep import Client
#7 https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL
#
#8  crear un servicio SOAP
#9  pip install pysimplesoap
#10.0 crear soap_server.py
#10 from http.server import HTTPServer
#11 from pysimplesoap.server import SoapDispatcher, SOAPHandler
#
#
#

from zeep import Client
client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
#peticion a el servicio soap 
result  = client.service.NumberToWords(5)
print(result)
#Tarea
result2 = client.service.NumberToDollars(0.2)
print(result2)
