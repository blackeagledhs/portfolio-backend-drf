# Portfolio Backend - SOLID

Este proyecto es una API backend diseñada para gestionar un portafolio personal. Es un proyecto basado en Django que sigue principios de diseño SOLID.

## Características
- **API RESTful** para manejar datos del portafolio (proyectos, experiencia, habilidades, etc.).
- Configuración optimizada para un solo usuario (no multiusuario).
- Diseño siguiendo los principios SOLID para facilitar la mantenibilidad y escalabilidad.
- Gestión de archivos estáticos para recursos como imágenes o documentos del portafolio.

## Funcionalidades

- Autenticación y autorización de usuarios.
- Operaciones CRUD para la gestión de portafolios.
- API REST para recuperar y actualizar datos del portafolio.
- Integración con frameworks frontend.
- Desplegado en un entorno en la nube.

## Estructura del Proyecto

- **blackeagle/**: Contiene la lógica de negocio de la API, incluyendo modelos, vistas y serializadores.
- **myportfolio/**: Archivos principales de configuración de Django (settings, urls).
- **static/** y **staticfiles/**: Directorios para archivos estáticos y preprocesados.
- **requirements.txt**: Dependencias necesarias para ejecutar el proyecto.

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

## Endpoints Disponibles

| Método  | Endpoint           | Descripción                                           |
|---------|--------------------|-------------------------------------------------------|
| **GET** | `/api/education/`   | Obtener todas las entradas de educación               |
| **POST**| `/api/education/`   | Crear una nueva entrada de educación                  |
| **GET** | `/api/experience/`  | Obtener todas las entradas de experiencia laboral     |
| **POST**| `/api/experience/`  | Crear una nueva entrada de experiencia laboral        |
| **GET** | `/api/projects/`    | Obtener todos los proyectos                           |
| **POST**| `/api/projects/`    | Crear un nuevo proyecto                               |
| **GET** | `/api/about/`       | Obtener información sobre el usuario ("Acerca de mí") |
| **POST**| `/api/about/`       | Crear o actualizar la información del usuario         |
| **GET** | `/api/badge/`       | Obtener todas las insignias                           |
| **POST**| `/api/badge/`       | Crear una nueva insignia                              |
| **GET** | `/api/other/`       | Obtener otras entradas relevantes                     |
| **POST**| `/api/other/`       | Crear una nueva entrada de "otros"                    |
| **GET** | `/api/extra/`       | Obtener información adicional                         |
| **POST**| `/api/extra/`       | Crear nueva información adicional                     |
| **GET** | `/api/contact/`     | Obtener información de contacto                       |
| **POST**| `/api/contact/`     | Crear o actualizar la información de contacto         |

La ruta raíz (/) redirige a una página en blanco (vista blank_page).​

## Principios SOLID

Este proyecto sigue los principios SOLID, que son:

1. **S**: Principio de Responsabilidad Única (Single Responsibility Principle)
2. **O**: Principio de Abierto/Cerrado (Open/Closed Principle)
3. **L**: Principio de Sustitución de Liskov (Liskov Substitution Principle)
4. **I**: Principio de Segregación de Interfaces (Interface Segregation Principle)
5. **D**: Principio de Inversión de Dependencias (Dependency Inversion Principle)

Estos principios se aplican en las vistas, modelos y serializadores para asegurar que cada clase tenga una única responsabilidad y sea fácil de extender sin modificar su comportamiento original.

## Contacto

Si tienes alguna duda o sugerencia, puedes contactarme a través de mi portafolio.

