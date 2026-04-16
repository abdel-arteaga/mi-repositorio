from flask import Blueprint, request, redirect, render_template
from tasks import send_email

main = Blueprint('main', __name__)

libros = []

@main.route('/')
def index():
    return render_template('index.html', libros=libros)

@main.route('/add', methods=['POST'])
def add_book():
    titulo = request.form['titulo']
    libros.append(titulo)

    send_email.delay(
        subject="Libro agregado",
        recipient="tu_correo@gmail.com",
        body=f"Se agregó el libro: {titulo}"
    )

    return redirect('/')

@main.route('/delete/<int:index>')
def delete_book(index):
    if 0 <= index < len(libros):
        eliminado = libros.pop(index)

        send_email.delay(
            subject="Libro eliminado",
            recipient="tu_correo@gmail.com",
            body=f"Se eliminó el libro: {eliminado}"
        )

    return redirect('/')