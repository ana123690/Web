from flask import Flask, redirect, render_template, request, url_for
from config import Config
from models import db, Usuario, Tarea
from sqlalchemy import *
app = Flask(__name__)
#Configuración de la aplicación Flask (donde se indica la base de datos a usar)
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)
# Crear la base de datos si no existe
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        if Usuario.query.filter_by(correo=correo).first():
            return "<script>alert('el correo ya esta reguistrado.')</scipt>"
        else:
            nuevo_usuario = Usuario(nombre=nombre,correo=correo)
            nuevo_usuario.colocar_contrasena(contrasena)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tasks')
def list_tasks():
    tareas = ["Lavar la ropa", "Limpiar la casa", "Hacer la compra", "Estudiar para el examen", "Hacer ejercicio", "Leer un libro"]
    return render_template('tasks.html', tareas=tareas)

@app.route('/task')
def view_task():
    return render_template('task.html')

@app.route('/task/create')
def create_task():
    return render_template('create_task.html')
#Crear una ruta y la vista correspondiente para renderizar un html llamado "create_task.html"



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)