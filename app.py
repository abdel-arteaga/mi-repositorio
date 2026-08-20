import os
from flask import Flask, jsonify, render_template_string
import mysql.connector

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>E-commerce AWS</title>
<style>
body{font-family:Arial,sans-serif;max-width:800px;margin:60px auto;padding:20px}
.card{border:1px solid #ddd;border-radius:10px;padding:24px;margin-top:20px}
.ok{color:#16803c}.error{color:#b42318}
</style>
</head>
<body>
<h1>E-commerce AWS</h1>
<p>Aplicación ejecutándose en Amazon ECS Fargate.</p>
<div class="card">
<h2>Estado de la aplicación</h2>
<p class="{{ css }}">{{ status }}</p>
<p>{{ detail }}</p>
</div>
</body>
</html>
"""

def get_db_config(include_database=True):
    config = {
        "host": os.environ["DB_HOST"],
        "port": int(os.environ.get("DB_PORT", "3306")),
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
        "connection_timeout": 5,
    }

    if include_database:
        config["database"] = os.environ["DB_NAME"]

    return config


def ensure_database():
    db_name = os.environ["DB_NAME"]

    conn = mysql.connector.connect(**get_db_config(include_database=False))
    cur = conn.cursor()

    cur.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")

    cur.close()
    conn.close()


def db_check():
    try:
        # Crea la base de datos si todavía no existe.
        ensure_database()

        # Ahora se conecta directamente a la base de datos.
        conn = mysql.connector.connect(
            **get_db_config(include_database=True)
        )

        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()

        cur.close()
        conn.close()

        return True, "Conexión a Amazon RDS MySQL: OK"

    except Exception as e:
        return False, f"RDS no disponible: {type(e).__name__}: {e}"


@app.get("/")
def index():
    ok, detail = db_check()

    return render_template_string(
        HTML,
        status=(
            "Aplicación y base de datos funcionando"
            if ok
            else "Aplicacion funcionando; RDS pendiente de conexión"
        ),
        detail=detail,
        css="ok" if ok else "error",
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/db-health")
def db_health():
    ok, detail = db_check()

    return jsonify({
        "database": "ok" if ok else "error",
        "detail": detail
    }), 200 if ok else 503


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000"))
    )
