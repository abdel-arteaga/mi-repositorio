from pymongo import MongoClient

def conectar():
    try:
        cliente = MongoClient(
            "mongodb+srv://abdelarteaga_db_user:rgBpA8AQQHtT5MCh@cluster-biblioteca.ya1f2w3.mongodb.net/?retryWrites=true&w=majority",
            serverSelectionTimeoutMS=5000
        )

        cliente.admin.command('ping')

        db = cliente["biblioteca"]
        coleccion = db["libros"]

        print("Conexión exitosa a MongoDB")
        return coleccion

    except Exception as e:
        print("Error de conexión:", e)
        return None