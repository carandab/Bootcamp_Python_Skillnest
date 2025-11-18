# Gestor de Tareas - Aplicación Web Django

## Descripción del Proyecto

Sistema de gestión de tareas desarrollado con Django que permite a los usuarios autenticarse y administrar sus tareas personales. Las tareas se almacenan en memoria durante la sesión.

---

## Estructura del Proyecto

```
gestor_tareas/
│
├── gestor_tareas/          # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py         # Configuraciones del proyecto
│   ├── urls.py             # URLs principales
│   ├── asgi.py
│   └── wsgi.py
│
├── tareas/                 # Aplicación de gestión de tareas
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Modelo de Tarea (no usado, memoria)
│   ├── views.py            # Vistas de la aplicación
│   ├── urls.py             # URLs de la aplicación
│   ├── forms.py            # Formularios Django
│   └── migrations/
│
├── templates/              # Plantillas HTML
│   ├── base.html           # Plantilla base con Bootstrap
│   ├── index.html          # Página de inicio
│   ├── registro/           # Plantillas de autenticación
│   │   ├── login.html
│   │   └── signup.html
│   └── tareas/             # Plantillas de tareas
│       ├── tareas_lista.html
│       ├── tareas_detalle.html
│       ├── tareas_agregar.html
│       └── tareas_eliminar.html
│
├── manage.py
└── db.sqlite3              # Base de datos SQLite
```

---

## Funcionalidades Implementadas

### 1. Sistema de Autenticación

- **Registro de usuarios**: Formulario personalizado con validación
- **Inicio de sesión**: Autenticación con django.contrib.auth
- **Cierre de sesión**: Logout seguro
- **Protección de vistas**: Decorador `@login_required`

### 2. Gestión de Tareas (En Memoria)

- **Listar tareas**: Vista de todas las tareas del usuario
- **Detalle de tarea**: Vista individual de cada tarea
- **Crear tarea**: Formulario Django para nueva tarea
- **Eliminar tarea**: Confirmación antes de eliminar
- **Privacidad**: Cada usuario solo ve sus propias tareas

### 3. Interfaz de Usuario

- **Bootstrap 5**: Diseño responsivo moderno
- **Bootstrap Icons**: Iconografía consistente
- **Alertas**: Mensajes de éxito/error con Django messages
- **Navegación**: Menú adaptativo según estado de autenticación

---

## Requisitos del Sistema

- Python 3.8 o superior
- Django 5.2 o superior
- pip (gestor de paquetes de Python)

---

## Instalación y Configuración

### 1. Crear y Activar Entorno Virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependencias

```bash
pip install django
```

### 3. Configurar la Base de Datos

```bash
python manage.py migrate
```

### 4. Crear Superusuario (Opcional)

```bash
python manage.py createsuperuser
```

### 5. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

---

## Uso de la Aplicación

### 1. Registro de Usuario

- Acceder a `/registro/`
- Completar el formulario con usuario, email y contraseña
- Confirmar la contraseña

### 2. Inicio de Sesión

- Acceder a `/login/`
- Ingresar usuario y contraseña
- Serás redirigido a la lista de tareas

### 3. Gestión de Tareas

- **Ver tareas**: `/tareas/`
- **Nueva tarea**: `/tareas/agregar/`
- **Ver detalle**: `/tareas/<id>/`
- **Eliminar**: `/tareas/<id>/eliminar/`

---

## Características Técnicas

### Almacenamiento en Memoria

Las tareas se almacenan en un diccionario global en `views.py`:

```python
TAREAS_MEMORIA = {
    user_id: [
        {'id': 1, 'titulo': '...', 'descripcion': '...', 'completada': False},
        # ... más tareas
    ]
}
```

**Nota**: Las tareas se pierden al reiniciar el servidor.

### Seguridad Implementada

- CSRF protection en todos los formularios
- Validación de usuarios autenticados
- Separación de tareas por usuario
- Validación de permisos en cada vista

### Forms Django

- `TareaForm`: Formulario para crear tareas
- `RegistroForm`: Formulario personalizado de registro basado en `UserCreationForm`

---

## Configuración para Producción

### 1. Configurar settings.py

```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']
SECRET_KEY = 'tu-clave-secreta-generada'
```

### 2. Generar Nueva Secret Key

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 3. Configurar Archivos Estáticos

```bash
python manage.py collectstatic
```

### 4. Usar Base de Datos de Producción

Para producción, considera PostgreSQL en lugar de SQLite:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Pruebas Realizadas

### Funcionalidad Probada

- ✅ Registro de usuarios
- ✅ Login/Logout
- ✅ Creación de tareas
- ✅ Visualización de lista de tareas
- ✅ Detalle individual de tarea
- ✅ Eliminación de tareas
- ✅ Separación de tareas por usuario
- ✅ Protección de vistas con @login_required
- ✅ Responsividad en móviles y tablets

---

## Limitaciones Conocidas

1. **Persistencia**: Las tareas se pierden al reiniciar el servidor
2. **Edición**: No implementada (solo crear, ver, eliminar)
3. **Búsqueda**: No hay funcionalidad de búsqueda
4. **Categorías**: No hay sistema de categorización
5. **Fechas límite**: No se manejan deadlines

---

## Mejoras Futuras

- [ ] Implementar modelo de Tarea con base de datos real
- [ ] Agregar funcionalidad de edición de tareas
- [ ] Sistema de categorías o etiquetas
- [ ] Fechas de vencimiento y recordatorios
- [ ] Búsqueda y filtros avanzados
- [ ] API REST para integración con aplicaciones móviles
- [ ] Tests unitarios y de integración

---

## Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5.3
- **Iconos**: Bootstrap Icons 1.10
- **Base de datos**: SQLite (desarrollo)
- **Autenticación**: django.contrib.auth

---

## Autor

Cristian Aranda Bórquez @carandab

## Licencia


Este proyecto es de uso educativo.
