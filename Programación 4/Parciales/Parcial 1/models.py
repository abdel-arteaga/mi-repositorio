import uuid

class Article:
    def __init__(self, nombre, categoria, cantidad, precio, descripcion):
        self.id = str(uuid.uuid4())  # 🔥 ID único
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = int(cantidad)
        self.precio = float(precio)
        self.descripcion = descripcion

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "cantidad": self.cantidad,
            "precio": self.precio,
            "descripcion": self.descripcion
        }