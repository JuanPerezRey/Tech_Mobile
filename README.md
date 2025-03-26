# Tech_Mobile
 API working with MYSQL database, it is a phone store where you can see the cell phones in inventory and also add cell phones.

Español:
Esta es mi API con base de datos MySQL sobre Tech_Mobile, una tienda de celulares ficticia. En primer lugar se usaron los mismos requerimientos usados abajo con la excepcion de MySQL debido a que PostgreSQL presentaba problemas al momento de ejecutarse la aplicación. Se actualizaron los siguientes archivos para quedar en concordancia con el tema de la tienda y que la aplicación no presentara problemas:

connection_py
estudiante_py
estudiantes_routes.py
index.html
base.html
agregar.html
editar.html
eliminar.html
listar.html
main.py
.env
init_db.py

English:
This is my API with MySQL database on Tech_Mobile, a fictitious mobile store. First of all the same requirements used below were used with the exception of MySQL because PostgreSQL presented problems when running the application. The following files were updated to match the theme of the store so that the application would not present problems:

connection_py
estudiante_py
estudiantes_routes.py
index.html
base.html
agregar.html
editar.html
eliminar.html
listar.html
main.py
.env
init_db.py

Pasos de Instalacion y Más Información - Installation Steps and More Information

# Proyecto Universidad

Este proyecto es una aplicación didáctica para la materia de **Base de Datos Web**. Utiliza **FastAPI** como framework, **SQLModel** como ORM, **PostgreSQL** como sistema de base de datos relacional (RDBMS) y **Jinja2** para las plantillas HTML. El objetivo es permitir realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una tabla de celulares.

## Descripción

El proyecto implementa una base de datos relacional llamada `tech_mobile`, que contiene una tabla llamada `estudiante`. Esta tabla tiene los siguientes atributos:

- `id`: Identificador único del celular.
- `marca`: Marca del celular.
- `modelo`: Modelo del celular.
- `almacenamientogb`: Espacio GB que tiene el celular.
- `precio`: Precio del celular.
- `stock`: Cantidad existente de stock en el inventario.

La aplicación permite realizar las operaciones CRUD sobre esta tabla de manera sencilla a través de una API construida con FastAPI.

## Tecnologías

- **FastAPI**: Framework web para crear APIs rápidas con Python.
- **SQLModel**: ORM para interactuar con bases de datos SQL utilizando Python.
- **MySQL**: Sistema de base de datos relacional.
- **Jinja2**: Motor de plantillas para generar HTML dinámico.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Python 3.x**
- **MySQL** (como sistema de gestión de bases de datos)
- **pip** (gestor de paquetes de Python)

## Instalación

Sigue estos pasos para instalar y configurar el proyecto:

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/stferraro/fastapi.git
    ```

2. **Acceder al directorio del proyecto**:
    ```bash
    cd mi-proyecto-universidad
    ```

3. **Crear y activar un entorno virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  
    En Windows usa venv\Scripts\activate.bat
    ```

4. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Configurar MySQL**:
    - Crea una base de datos llamada `tech_mobile` en MySQL.
    - Configura los parámetros de conexión en un archivo `.env` con la siguiente configuración:

    ```
    DB_USER=root
    DB_PASSWORD=J321
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=tech_mobile
    DB_DRIVER=mysql+pymysql
    ```

6. **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    fastapi dev app/main.py
    ```

    La aplicación estará disponible en `http://localhost:8000`.

## Uso

La API permite realizar las operaciones CRUD sobre la tabla `estudiante`. A continuación se muestran las rutas disponibles:

- **Crear celulares**: `POST /celulares`
- **Leer celulares**: `GET /celulares`
- **Actualizar celulares**: `PUT /celulares/{id}`
- **Eliminar celulares**: `DELETE /celulares/{id}`

Además, puedes acceder a una interfaz web con plantillas generadas con **Jinja2**.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama para tu característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Envía un pull request para revisión.

## Licencia

Este proyecto está bajo la Licencia GPL-3.0 - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

# University Project

This project is an educational application for the **Web Database** course. It uses **FastAPI** as the framework, **SQLModel** as the ORM, **MySQL** as the relational database system (RDBMS), and **Jinja2** for HTML templates. The goal is to allow performing CRUD operations (Create, Read, Update, Delete) on a student table.

## Description

The project implements a relational database called `tech_mobile`, which contains a table called `student`. This table has the following attributes:

- `id`: Unique identifier for the student.
- `marca`: Name of the student.
- `modelo`: Last name of the student.
- `almacenamiento`: Unique student code.
- `precio`: Gender of the student.
- `stock`: Age of the student.

The application allows performing CRUD operations on this table in a simple way via an API built with FastAPI.

## Technologies

- **FastAPI**: Web framework for creating fast APIs with Python.
- **SQLModel**: ORM for interacting with SQL databases using Python.
- **MySQL**: Relational database management system.
- **Jinja2**: Template engine for generating dynamic HTML.

## Requirements

Before you begin, make sure you have the following installed:

- **Python 3.x**
- **MySQL** (as the database management system)
- **pip** (Python package manager)

## Installation

Follow these steps to install and set up the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/stferraro/fastapi.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd tech_mobile-project
    ```

3. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   
    On Windows use venv\Scripts\activate.bat
    ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure MySQL**:
    - Create a database called `tech_mobile` in MySQL.
    - Configure the connection parameters in a `.env` file with the following settings:

    ```
    DB_USER=root
    DB_PASSWORD=J321
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=tech_mobile
    DB_DRIVER=mysql+pymysql
    ```

6. **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    fastapi dev app/main.py
    ```

    The application will be available at `http://localhost:8000`.

## Usage

The API allows performing CRUD operations on the `student` table. The available routes are:

- **Create cellphone**: `POST /cellphone`
- **Read cellphone**: `GET /cellphone`
- **Update cellphone**: `PUT /cellphone/{id}`
- **Delete cellphone**: `DELETE /cellphone/{id}`

Additionally, you can access a web interface with templates generated using **Jinja2**.

## Contribute

If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Send a pull request for review.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for more details.
