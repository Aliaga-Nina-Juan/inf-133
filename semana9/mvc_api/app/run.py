from flask import Flask
from controllers.animal_controller import animal_bp
from database import db

app = Flask(__name__)

#Configuracion de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zoo.db"
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la base de datos
db.init_app(app)

#Registra el blueprint de animales en la aplicacion
app.register_blueprint(animal_bp,url_prefix="/api")

#Crea las tablas si no existen
with app.app_context():
    db.create_all()
    
#Ejecuta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)