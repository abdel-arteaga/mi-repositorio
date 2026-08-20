# ecommerce-app

Aplicación de prueba para la arquitectura AWS del proyecto.

Arquitectura:
Internet -> Application Load Balancer -> ECS Fargate -> RDS MySQL

Endpoints:
- / : página principal
- /health : health check del contenedor
- /db-health : prueba de conexión con RDS

Variables de entorno:
DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

Las credenciales se configurarán en ECS y no se guardarán en el código.
