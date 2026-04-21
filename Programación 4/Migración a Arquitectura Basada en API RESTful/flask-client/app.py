from flask import Flask, render_template, request, redirect, flash
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    try:
        res = requests.get(f"{API_URL}/books", timeout=5)
        res.raise_for_status()
        books = res.json()
    except:
        books = []
        flash("Error conectando con API")

    return render_template("index.html", books=books)


@app.route("/add", methods=["POST"])
def add_book():
    data = {
        "titulo": request.form["titulo"],
        "autor": request.form["autor"],
        "genero": request.form["genero"],
        "estado": request.form["estado"]
    }

    try:
        res = requests.post(f"{API_URL}/books", json=data)
        if res.status_code == 201:
            flash("Libro agregado")
        else:
            flash("Error al agregar")
    except:
        flash("Error de conexión")

    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    try:
        res = requests.delete(f"{API_URL}/books/{id}")
        if res.status_code == 200:
            flash("Eliminado correctamente")
        else:
            flash("Error al eliminar")
    except:
        flash("Error de conexión")

    return redirect("/")


if __name__ == "__main__":
    app.run(port=5001, debug=True)