import sqlite3
from typing import Optional

DB_NAME = "biblioteca.db"


# ----------------------------
# Conexión y creación de tabla
# ----------------------------

def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def crear_tabla():
    with conectar() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            estado TEXT NOT NULL CHECK(estado IN ('Leído','No leído'))
        );
        """)
        conn.commit()


# ----------------------------
# Funciones CRUD
# ----------------------------

def agregar_libro():
    print("\n=== Agregar nuevo libro ===")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Género: ").strip()

    while True:
        estado = input("Estado (Leído/No leído): ").strip()
        if estado in ("Leído", "No leído"):
            break
        print("Estado inválido. Use 'Leído' o 'No leído'.")

    with conectar() as conn:
        conn.execute(
            "INSERT INTO libros (titulo, autor, genero, estado) VALUES (?, ?, ?, ?)",
            (titulo, autor, genero, estado)
        )
        conn.commit()

    print("Libro agregado correctamente.")


def listar_libros():
    print("\n=== Lista de libros ===")
    with conectar() as conn:
        cursor = conn.execute("SELECT * FROM libros")
        libros = cursor.fetchall()

    if not libros:
        print("No hay libros registrados.")
        return

    for libro in libros:
        print(f"""
ID: {libro[0]}
Título: {libro[1]}
Autor: {libro[2]}
Género: {libro[3]}
Estado: {libro[4]}
----------------------------
""")


def actualizar_libro():
    listar_libros()
    try:
        libro_id = int(input("Ingrese ID del libro a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    with conectar() as conn:
        cursor = conn.execute("SELECT * FROM libros WHERE id = ?", (libro_id,))
        libro = cursor.fetchone()

        if not libro:
            print("Libro no encontrado.")
            return

        print("Deje vacío para mantener el valor actual.")

        titulo = input(f"Título [{libro[1]}]: ").strip() or libro[1]
        autor = input(f"Autor [{libro[2]}]: ").strip() or libro[2]
        genero = input(f"Género [{libro[3]}]: ").strip() or libro[3]

        estado_input = input(f"Estado [{libro[4]}] (Leído/No leído): ").strip()
        estado = estado_input if estado_input in ("Leído", "No leído") else libro[4]

        conn.execute("""
            UPDATE libros
            SET titulo = ?, autor = ?, genero = ?, estado = ?
            WHERE id = ?
        """, (titulo, autor, genero, estado, libro_id))
        conn.commit()

    print("Libro actualizado correctamente.")


def eliminar_libro():
    listar_libros()
    try:
        libro_id = int(input("Ingrese ID del libro a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    with conectar() as conn:
        conn.execute("DELETE FROM libros WHERE id = ?", (libro_id,))
        conn.commit()

    print("Libro eliminado correctamente.")


def buscar_libros():
    print("\n=== Buscar libros ===")
    criterio = input("Buscar por (titulo/autor/genero): ").strip().lower()

    if criterio not in ("titulo", "autor", "genero"):
        print("Criterio inválido.")
        return

    valor = input("Ingrese término de búsqueda: ").strip()

    with conectar() as conn:
        cursor = conn.execute(
            f"SELECT * FROM libros WHERE {criterio} LIKE ?",
            (f"%{valor}%",)
        )
        resultados = cursor.fetchall()

    if not resultados:
        print("No se encontraron resultados.")
        return

    for libro in resultados:
        print(f"""
ID: {libro[0]}
Título: {libro[1]}
Autor: {libro[2]}
Género: {libro[3]}
Estado: {libro[4]}
----------------------------
""")


# ----------------------------
# Menú principal
# ----------------------------

def menu():
    while True:
        print("""
===== Biblioteca Personal =====
1) Agregar libro
2) Actualizar libro
3) Eliminar libro
4) Ver libros
5) Buscar libros
0) Salir
""")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            actualizar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            listar_libros()
        elif opcion == "5":
            buscar_libros()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    crear_tabla()
    menu()
