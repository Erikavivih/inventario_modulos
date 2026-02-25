 from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100))

    categoria = db.Column(db.String(50))

    precio = db.Column(db.Float)

    stock = db.Column(db.Integer)
