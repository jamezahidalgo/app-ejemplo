# app-ejemplo
Proyecto base ASY4131

+ La aplicación está diseñada para ser sencilla, pero modular, lo que permite su escalabilidad y fácil mantenimiento.
+ Se utiliza SQLite como base de datos para simplificar la implementación, pero la aplicación puede adaptarse fácilmente a otros motores de bases de datos.

Arquitectura de la aplicación

+ Programación por Capas: El código está organizado en capas que separan la lógica de negocios (servicios), la interacción con la base de datos (modelos), el manejo de las solicitudes HTTP (controladores) y la presentación de las rutas (vistas).
+ Patrón Singleton: Se asegura que la conexión a la base de datos sea única y se reutilice en toda la aplicación.
+ ORM con SQLAlchemy: Se utiliza SQLAlchemy para mapear las clases de Python a las tablas de la base de datos, facilitando la interacción con la base de datos.

