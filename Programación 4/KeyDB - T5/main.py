import redis
import json
import os
from dotenv import load_dotenv

# ----------------------------
# Configuración y conexión
# ----------------------------

load_dotenv()

r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

# Validar conexión
try:
    r.ping()
except redis.ConnectionError:
    print("Error: no se pudo conectar a KeyDB.")
    exit()


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

    libro_id = r.incr("contador_libros")

    libro = {
        "id": libro_id,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estado": estado
    }

    r.set(f"libro:{libro_id}", json.dumps(libro))

    print("Libro agregado correctamente.")


def listar_libros():
    print("\n=== Lista de libros ===")

    keys = list(r.scan_iter("libro:*"))

    if not keys:
        print("No hay libros registrados.")
        return

    for key in keys:
        libro = json.loads(r.get(key))

        print(f"""
ID: {libro['id']}
Título: {libro['titulo']}
Autor: {libro['autor']}
Género: {libro['genero']}
Estado: {libro['estado']}
----------------------------
""")


def buscar_libros():
    print("\n=== Buscar libros ===")
    criterio = input("Buscar por (titulo/autor/genero): ").strip().lower()

    if criterio not in ("titulo", "autor", "genero"):
        print("Criterio inválido.")
        return

    valor = input("Ingrese término de búsqueda: ").strip().lower()

    encontrados = False

    for key in r.scan_iter("libro:*"):
        libro = json.loads(r.get(key))

        if valor in libro[criterio].lower():
            encontrados = True
            print(f"""
ID: {libro['id']}
Título: {libro['titulo']}
Autor: {libro['autor']}
Género: {libro['genero']}
Estado: {libro['estado']}
----------------------------
""")

    if not encontrados:
        print("No se encontraron resultados.")


def actualizar_libro():
    listar_libros()

    try:
        libro_id = int(input("Ingrese ID del libro a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    key = f"libro:{libro_id}"

    if not r.exists(key):
        print("Libro no encontrado.")
        return

    libro = json.loads(r.get(key))

    print("Deje vacío para mantener el valor actual.")

    titulo = input(f"Título [{libro['titulo']}]: ").strip() or libro["titulo"]
    autor = input(f"Autor [{libro['autor']}]: ").strip() or libro["autor"]
    genero = input(f"Género [{libro['genero']}]: ").strip() or libro["genero"]

    estado_input = input(f"Estado [{libro['estado']}] (Leído/No leído): ").strip()
    estado = estado_input if estado_input in ("Leído", "No leído") else libro["estado"]

    libro_actualizado = {
        "id": libro_id,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estado": estado
    }

    r.set(key, json.dumps(libro_actualizado))

    print("Libro actualizado correctamente.")


def eliminar_libro():
    listar_libros()

    try:
        libro_id = int(input("Ingrese ID del libro a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    if r.delete(f"libro:{libro_id}"):
        print("Libro eliminado correctamente.")
    else:
        print("Libro no encontrado.")


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


# ----------------------------
# Main
# ----------------------------

if __name__ == "__main__":
    menu()