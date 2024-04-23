# Importa la clase Flask del paquet flask
from flask import Flask, request,jsonify

app = Flask(__name__)
@app.route('/')
def hello_word():
    return 'Hola, mundo!'
@app.route('/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return(
            jsonify({"error":"Se requiere un nombre de los parametros de la URL"}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route('/sumar',methods=['GET'])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    num1 = int(num1)
    num2 = int(num2)
    
    if not num1:
        return(
            jsonify({"error":"Se requiere de dos parametros en la URL"}),
            400,
        )
    return jsonify({"mensaje":f"La suma de {num1}+{num2} es {num1+num2}"})

@app.route('/palindromo',methods=['GET'])
def palindromo():
    cadena = request.args.get("palindromo")
    cadena_reversa = cadena[::-1]
    if(cadena==cadena_reversa):
        return jsonify({"mensaje":f"La cadena {cadena} si es un palindromo"})
    else:
        return jsonify({"mensaje":f"La cadena {cadena} no es un palindromo"})
    
@app.route('/contar_vocales',methods=['GET'])
def contar_vocales():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    con = 0
    for row in cadena:
        if vocal == row:
            con = con + 1
    return jsonify({"mensaje":f"La cadena {cadena} tiene {con} vocales {vocal}"})
#Definimos como se levantara el servidor
if __name__ == '__main__':
    app.run()
    

