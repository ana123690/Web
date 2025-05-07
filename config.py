import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Para usar PostgreSQL, cambiar a:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:contraseña@localhost/nombre_base_datos'
    # Para usar MySQL, cambiar a:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:contraseña@localhost/nombre_base_datos'
    # Configuración de conexión a la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Clave secreta para sesiones (crear una única para producción)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mi-clave-secreta'