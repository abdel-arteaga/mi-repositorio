from models import Article
from storage import load_data, save_data
from utils import input_no_vacio, input_numero

def registrar():
    data = load_data()

    nombre = input_no_vacio("Nombre: ")
    categoria = input_no_vacio("Categoría: ")
    cantidad = input_numero("Cantidad: ", int)
    precio = input_numero("Precio unitario: ", float)
    descripcion = input("Descripción: ")

    art = Article(nombre, categoria, cantidad, precio, descripcion)
    data.append(art.to_dict())
    save_data(data)

    print("Artículo registrado.")

def listar():
    data = load_data()
    if not data:
        print("No hay artículos.")
        return

    print("\n--- LISTA DE ARTÍCULOS ---")
    for a in data:
        print(f"{a['id'][:6]} | {a['nombre']} | {a['categoria']} | {a['cantidad']} | ${a['precio']}")

def buscar():
    data = load_data()
    criterio = input("Buscar por nombre o categoría: ").lower()

    resultados = [a for a in data if criterio in a['nombre'].lower() or criterio in a['categoria'].lower()]

    if resultados:
        for a in resultados:
            print(a)
    else:
        print("No encontrado.")

def editar():
    data = load_data()
    id_buscar = input("ID del artículo: ")

    for a in data:
        if a['id'].startswith(id_buscar):
            print("Editando:", a)

            a['cantidad'] = input_numero("Nueva cantidad: ", int)
            a['precio'] = input_numero("Nuevo precio: ", float)

            save_data(data)
            print("✅ Actualizado.")
            return

    print("No encontrado.")

def eliminar():
    data = load_data()
    id_buscar = input("ID a eliminar: ")

    nuevo = [a for a in data if not a['id'].startswith(id_buscar)]

    if len(nuevo) == len(data):
        print("No encontrado.")
    else:
        save_data(nuevo)
        print("🗑Eliminado.")

def menu():
    while True:
        print("""
1. Registrar
2. Listar
3. Buscar
4. Editar
5. Eliminar
0. Salir
""")
        op = input("Opción: ")

        if op == "1":
            registrar()
        elif op == "2":
            listar()
        elif op == "3":
            buscar()
        elif op == "4":
            editar()
        elif op == "5":
            eliminar()
        elif op == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()