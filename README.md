# Portfolio Backend - SOLID

Este proyecto es una aplicación backend diseñada utilizando principios de Django y Django REST Framework (DRF), con el objetivo de gestionar el contenido del portfolio. El código sigue los principios SOLID para garantizar mantenibilidad, escalabilidad y robustez.

## Funcionalidades

- Autenticación y autorización de usuarios.
- Operaciones CRUD para la gestión de portafolios.
- API REST para recuperar y actualizar datos del portafolio.
- Integración con frameworks frontend.
- Desplegado en un entorno en la nube.

## Tecnologías Usadas

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL (o cualquier sistema de bases de datos preferido)
- Docker (opcional, para la contenedorización)

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu máquina:

- [Python 3.x](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/) o tu sistema de base de datos preferido.
- [Pipenv](https://pipenv.pypa.io/en/latest/) o [virtualenv](https://virtualenv.pypa.io/en/stable/) para gestionar dependencias.

## Instalación

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/yourusername/portfolio-backend-solid.git
    cd portfolio-backend-solid
    ```

2. Crear y activar un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows, usa `venv\\Scripts\\activate`
    ```

3. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configurar la base de datos en `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nombre_de_tu_bd',
            'USER': 'usuario_de_tu_bd',
            'PASSWORD': 'contraseña_de_tu_bd',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Aplicar migraciones y ejecutar el servidor:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Endpoints de la API



## Estructura del Proyecto

