from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"

DB_NAME = "biblioteca.db"

def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# -------------------------
# RUTAS
# -------------------------

@app.route("/")
def index():
    conn = conectar()
    libros = conn.execute("SELECT * FROM libros").fetchall()
    conn.close()
    return render_template("index.html", libros=libros)


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        genero = request.form["genero"]
        estado = request.form["estado"]

        conn = conectar()
        conn.execute(
            "INSERT INTO libros (titulo, autor, genero, estado) VALUES (?, ?, ?, ?)",
            (titulo, autor, genero, estado)
        )
        conn.commit()
        conn.close()

        flash("Libro agregado correctamente")
        return redirect(url_for("index"))

    return render_template("agregar.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = conectar()
    libro = conn.execute("SELECT * FROM libros WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        genero = request.form["genero"]
        estado = request.form["estado"]

        conn.execute("""
            UPDATE libros
            SET titulo=?, autor=?, genero=?, estado=?
            WHERE id=?
        """, (titulo, autor, genero, estado, id))
        conn.commit()
        conn.close()

        flash("Libro actualizado")
        return redirect(url_for("index"))

    conn.close()
    return render_template("editar.html", libro=libro)


@app.route("/eliminar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    conn = conectar()
    libro = conn.execute("SELECT * FROM libros WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        conn.execute("DELETE FROM libros WHERE id = ?", (id,))
        conn.commit()
        conn.close()

        flash("Libro eliminado")
        return redirect(url_for("index"))

    conn.close()
    return render_template("eliminar.html", libro=libro)


@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultados = []

    if request.method == "POST":
        criterio = request.form["criterio"]
        valor = request.form["valor"]

        conn = conectar()
        query = f"SELECT * FROM libros WHERE {criterio} LIKE ?"
        resultados = conn.execute(query, (f"%{valor}%",)).fetchall()
        conn.close()

    return render_template("buscar.html", resultados=resultados)


if __name__ == "__main__":
    app.run(debug=True)
