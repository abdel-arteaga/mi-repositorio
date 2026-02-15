from database import SessionLocal, init_db
from modelo import Libro
from sqlalchemy.exc import SQLAlchemyError

init_db()
session = SessionLocal()

def agregar_libro():
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        estado = input("Estado (Leído/No leído): ")

        nuevo = Libro(
            titulo=titulo,
            autor=autor,
            genero=genero,
            estado=estado
        )

        session.add(nuevo)
        session.commit()
        print("Libro agregado correctamente.")

    except SQLAlchemyError as e:
        session.rollback()
        print("Error al agregar libro:", e)

def ver_libros():
    libros = session.query(Libro).all()
    for libro in libros:
        print(f"{libro.id} - {libro.titulo} | {libro.autor} | {libro.genero} | {libro.estado}")

def eliminar_libro():
    try:
        id_libro = int(input("ID del libro a eliminar: "))
        libro = session.get(Libro, id_libro)

        if libro:
            session.delete(libro)
            session.commit()
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    except SQLAlchemyError as e:
        session.rollback()
        print("Error:", e)

def actualizar_libro():
    try:
        id_libro = int(input("ID del libro a actualizar: "))
        libro = session.get(Libro, id_libro)

        if libro:
            libro.titulo = input("Nuevo título: ")
            libro.autor = input("Nuevo autor: ")
            libro.genero = input("Nuevo género: ")
            libro.estado = input("Nuevo estado: ")

            session.commit()
            print("Libro actualizado.")
        else:
            print("Libro no encontrado.")

    except SQLAlchemyError as e:
        session.rollback()
        print("Error:", e)

def buscar_libros():
    termino = input("Buscar por título, autor o género: ")

    resultados = session.query(Libro).filter(
        (Libro.titulo.like(f"%{termino}%")) |
        (Libro.autor.like(f"%{termino}%")) |
        (Libro.genero.like(f"%{termino}%"))
    ).all()

    for libro in resultados:
        print(f"{libro.id} - {libro.titulo} | {libro.autor}")

def menu():
    while True:
        print("\n--- Biblioteca ORM MariaDB ---")
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
