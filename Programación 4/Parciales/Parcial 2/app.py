from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

# -------------------------
# GET /vacunas
# -------------------------
@app.route("/vacunas", methods=["GET"])
def obtener_todo():
    data = load_data()
    return jsonify(data)

# -------------------------
# GET /vacunas/<año>
# -------------------------
@app.route("/vacunas/<int:anio>", methods=["GET"])
def obtener_por_anio(anio):
    data = load_data()

    for registro in data:
        if registro["anio"] == anio:
            return jsonify(registro)

    return jsonify({"error": "Año no encontrado"}), 404

# -------------------------
# (OPCIONAL) provincia
# -------------------------
@app.route("/vacunas/provincia/<nombre>", methods=["GET"])
def por_provincia(nombre):
    data = load_data()

    # Simulación simple
    return jsonify({
        "provincia": nombre,
        "datos": data
    })

# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)