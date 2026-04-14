Este proyecto consiste en una aplicación de línea de comandos desarrollada en Python para la gestión de una biblioteca personal, utilizando MongoDB como base de datos no relacional mediante el cliente oficial pymongo.

El sistema permite realizar operaciones CRUD (crear, leer, actualizar y eliminar) sobre una colección de libros, donde cada libro se almacena como un documento en formato JSON con los campos título, autor, género y estado de lectura. A diferencia de las bases de datos relacionales, no se utiliza un esquema fijo, lo que brinda mayor flexibilidad en la gestión de los datos.

Para su funcionamiento, es necesario instalar las dependencias indicadas en el archivo requirements.txt y configurar una conexión a MongoDB, ya sea local o mediante MongoDB Atlas. La aplicación se ejecuta desde la terminal con el comando python app.py, mostrando un menú interactivo para acceder a las distintas funcionalidades.

El programa incluye validaciones básicas para el manejo de errores, como problemas de conexión, datos incompletos y búsquedas sin resultados.

En conclusión, este proyecto demuestra la implementación de una aplicación CRUD utilizando un enfoque no relacional, destacando la simplicidad y flexibilidad que ofrece MongoDB en comparación con los sistemas tradicionales basados en tablas.
