from flask import Flask, render_template, request, redirect, url_for, flash
import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Conexión KeyDB
r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)

# ----------------------------
# Helpers (equivalente a SELECT *)
# ----------------------------

def obtener_libros():
    libros = []
    for key in r.scan_iter("libro:*"):
        libros.append(json.loads(r.get(key)))
    return libros


# ----------------------------
# Rutas (equivalente al menú)
# ----------------------------

@app.route("/")
def index():
    libros = obtener_libros()
    return render_template("index.html", libros=libros)


@app.route("/agregar", methods=["GET", "POST"])
def agregar_libro():
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        genero = request.form["genero"].strip()
        estado = request.form["estado"].strip()

        # Validación igual que tu código original
        if estado not in ("Leído", "No leído"):
            flash("Estado inválido.")
            return redirect(url_for("agregar_libro"))

        libro_id = r.incr("contador_libros")

        libro = {
            "id": libro_id,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "estado": estado
        }

        r.set(f"libro:{libro_id}", json.dumps(libro))

        flash("Libro agregado correctamente.")
        return redirect(url_for("index"))

    return render_template("agregar.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def actualizar_libro(id):
    key = f"libro:{id}"

    if not r.exists(key):
        flash("Libro no encontrado.")
        return redirect(url_for("index"))

    libro = json.loads(r.get(key))

    if request.method == "POST":
        titulo = request.form["titulo"].strip() or libro["titulo"]
        autor = request.form["autor"].strip() or libro["autor"]
        genero = request.form["genero"].strip() or libro["genero"]

        estado_input = request.form["estado"].strip()
        estado = estado_input if estado_input in ("Leído", "No leído") else libro["estado"]

        libro_actualizado = {
            "id": id,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "estado": estado
        }

        r.set(key, json.dumps(libro_actualizado))

        flash("Libro actualizado correctamente.")
        return redirect(url_for("index"))

    return render_template("editar.html", libro=libro)


@app.route("/eliminar/<int:id>")
def eliminar_libro(id):
    r.delete(f"libro:{id}")
    flash("Libro eliminado correctamente.")
    return redirect(url_for("index"))


@app.route("/buscar")
def buscar_libros():
    valor = request.args.get("q", "").lower()

    resultados = []

    for key in r.scan_iter("libro:*"):
        libro = json.loads(r.get(key))

        if (
            valor in libro["titulo"].lower()
            or valor in libro["autor"].lower()
            or valor in libro["genero"].lower()
        ):
            resultados.append(libro)

    if not resultados:
        flash("No se encontraron resultados.")

    return render_template("index.html", libros=resultados)


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    app.run(debug=True)
