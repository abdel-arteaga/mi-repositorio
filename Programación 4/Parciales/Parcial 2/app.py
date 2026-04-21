from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_data():
    with open("data.json") as f:
        return json.load(f)

@app.route("/vacunas", methods=["GET"])
def get_all():
    return jsonify(load_data())

@app.route("/vacunas/<int:year>", methods=["GET"])
def get_by_year(year):
    data = load_data()
    for d in data:
        if d["year"] == year:
            return jsonify(d)
    return jsonify({"error": "No encontrado"}), 404

@app.route("/vacunas/provincia/<nombre>", methods=["GET"])
def get_by_provincia(nombre):
    data = load_data()
    simulated = [
        {
            "provincia": nombre,
            "year": d["year"],
            "coverage": d["coverage"] - 2
        }
        for d in data
    ]
    return jsonify(simulated)

if __name__ == "__main__":
    app.run(debug=True)