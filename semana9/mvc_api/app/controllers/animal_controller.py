from flask import Blueprint, request, jsonify
from models.animal_model import Animal
from views.animal_view import render_animal_list, render_animal_detail

# Crear un blueprint para el controlador de animales
animal_bp = Blueprint("animal", __name__)

# Ruta para obtener la lista de animales
@animal_bp.route("/animals", methods=["GET"])
def get_animals():
    animals = Animal.get_all()
    return jsonify(render_animal_list(animals))

# Ruta para obtener un animal especifico por su ID
@animal_bp.route("/animals/<int:id>",methods=["GET"])
def get_animal(id):
    animal = Animal.get_by_id(id)
    if animal:
        return jsonify(render_animal_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404

#Ruta para crear un nuevo animal
@animal_bp.route("animals",methods=["POST"])
def create_animal():
    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")
    
    #Validacion simple de datos de entrada
    if not name or not species or age is None:
        return jsonify({"error": "Faltan datos requeridos"}),404
    #Crear un nuevo animal y guardarlo en la base de datos
    animal = Animal(name=name,species=species,age=age)
    animal.save()
    
    return jsonify(render_animal_detail(animal)),201

#Ruta para actualizar un animal existente
@animal_bp.route("/animals/<int:id>",methods=["PUT"])
def update_animal(id):
    animal = Animal.get_by_id(id)
    
    if not animal:
        return jsonify({"error": "Animal no encontrado"}),404
    data = request.json
    name = data.get("name")
    species = data.get("species")
    age = data.get("age")
    
    #Actualizar los datos del animal
    animal.update(name=name,species=species,age=age)
    
    return jsonify(render_animal_detail(animal))

#Ruta para eliminar un animal
@animal_bp.route("/animals/<int:id>",methods=["DELETE"])
def delete_animal(id):
    animal = Animal.get_by_id(id)
    
    if not animal:
        return jsonify({"error": "Animal no encontrado"}),404
    
    #Eliminar un animal de la base de datos
    animal.delete()
    #Respuesta vacia con codigo de estado 204 (sin contenido)
    return "",204

