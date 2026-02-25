 from models.producto import db, Producto

class InventarioService:

    def listar_productos():

        return Producto.query.all()


    def agregar_producto(nombre,categoria,precio,stock):

        producto = Producto(

            nombre = nombre,
            categoria = categoria,
            precio = precio,
            stock = stock

        )

        db.session.add(producto)

        db.session.commit()
