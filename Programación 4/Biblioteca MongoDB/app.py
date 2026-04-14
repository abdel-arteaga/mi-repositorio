from db import conectar
from bson import ObjectId

coleccion = conectar()

# -------------------------
# AGREGAR LIBRO
# -------------------------
def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado = input("Estado (Leído/No leído): ")

    if not titulo or not autor:
        print("Datos inválidos")
        return

    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estado": estado
    }

    coleccion.insert_one(libro)
    print("Libro agregado correctamente.")


# -------------------------
# VER LIBROS
# -------------------------
def ver_libros():
    libros = coleccion.find()

    for libro in libros:
        print(f"{libro['_id']} - {libro['titulo']} | {libro['autor']} | {libro['genero']} | {libro['estado']}")


# -------------------------
# ELIMINAR LIBRO
# -------------------------
def eliminar_libro():
    id_libro = input("ID del libro a eliminar: ")

    resultado = coleccion.delete_one({
        "_id": ObjectId(id_libro)
    })

    if resultado.deleted_count > 0:
        print("Libro eliminado.")
    else:
        print("Libro no encontrado.")


# -------------------------
# ACTUALIZAR LIBRO
# -------------------------
def actualizar_libro():
    id_libro = input("ID del libro a actualizar: ")

    nuevo_titulo = input("Nuevo título: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_genero = input("Nuevo género: ")
    nuevo_estado = input("Nuevo estado: ")

    resultado = coleccion.update_one(
        {"_id": ObjectId(id_libro)},
        {
            "$set": {
                "titulo": nuevo_titulo,
                "autor": nuevo_autor,
                "genero": nuevo_genero,
                "estado": nuevo_estado
            }
        }
    )

    if resultado.modified_count > 0:
        print("Libro actualizado.")
    else:
        print("Libro no encontrado o sin cambios.")


# -------------------------
# BUSCAR LIBROS
# -------------------------
def buscar_libros():
    termino = input("Buscar por título, autor o género: ")

    resultados = coleccion.find({
        "$or": [
            {"titulo": {"$regex": termino, "$options": "i"}},
            {"autor": {"$regex": termino, "$options": "i"}},
            {"genero": {"$regex": termino, "$options": "i"}}
        ]
    })

    encontrados = False

    for libro in resultados:
        encontrados = True
        print(f"{libro['_id']} - {libro['titulo']} | {libro['autor']}")

    if not encontrados:
        print("No se encontraron resultados.")


# -------------------------
# MENÚ
# -------------------------
def menu():
    if not coleccion:
        print("Error de conexión con la base de datos")
        return

    while True:
        print("\n--- Biblioteca MongoDB ---")
        print("1. Agregar libro")
        print("2. Ver libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Buscar libro")
        print("6. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            ver_libros()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            buscar_libros()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()