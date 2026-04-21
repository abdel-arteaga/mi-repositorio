from flask import Flask, request, jsonify
from db import conectar, init_db

app = Flask(__name__)


@app.route("/books", methods=["GET"])
def get_books():
    conn = conectar()
    books = conn.execute("SELECT * FROM libros").fetchall()
    return jsonify([dict(book) for book in books]), 200


@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    conn = conectar()
    book = conn.execute("SELECT * FROM libros WHERE id = ?", (id,)).fetchone()

    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404

    return jsonify(dict(book)), 200


@app.route("/books", methods=["POST"])
def create_book():
    data = request.json

    if not data or not all(k in data for k in ("titulo","autor","genero","estado")):
        return jsonify({"error": "Datos incompletos"}), 400

    conn = conectar()
    cursor = conn.execute("""
        INSERT INTO libros (titulo, autor, genero, estado)
        VALUES (?, ?, ?, ?)
    """, (
        data["titulo"],
        data["autor"],
        data["genero"],
        data["estado"]
    ))
    conn.commit()

    return jsonify({"id": cursor.lastrowid}), 201


@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.json

    conn = conectar()
    book = conn.execute("SELECT * FROM libros WHERE id = ?", (id,)).fetchone()

    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404

    conn.execute("""
        UPDATE libros
        SET titulo=?, autor=?, genero=?, estado=?
        WHERE id=?
    """, (
        data.get("titulo", book["titulo"]),
        data.get("autor", book["autor"]),
        data.get("genero", book["genero"]),
        data.get("estado", book["estado"]),
        id
    ))
    conn.commit()

    return jsonify({"msg": "Actualizado"}), 200


@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    conn = conectar()
    conn.execute("DELETE FROM libros WHERE id = ?", (id,))
    conn.commit()

    return jsonify({"msg": "Eliminado"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)