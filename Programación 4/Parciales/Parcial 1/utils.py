def input_no_vacio(msg):
    while True:
        val = input(msg).strip()
        if val:
            return val
        print("Campo no puede estar vacío.")

def input_numero(msg, tipo=float):
    while True:
        try:
            return tipo(input(msg))
        except ValueError:
            print("Ingresa un número válido.")