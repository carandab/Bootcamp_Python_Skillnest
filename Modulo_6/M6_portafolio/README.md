# TaskManager Pro 📋

Sistema de gestión de tareas desarrollado con Django como parte del portafolio de desarrollo web empresarial.

![Django](https://img.shields.io/badge/Django-5.2-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

## 📖 Descripción

TaskManager Pro es una aplicación web completa para la gestión y organización de tareas personales. Permite a los usuarios crear, editar, eliminar y categorizar sus tareas con diferentes niveles de prioridad y estados de completitud.

Este proyecto fue desarrollado como parte de la evaluación de portafolio del curso de Django, implementando todas las competencias técnicas requeridas para el desarrollo de aplicaciones empresariales con Django.

## ✨ Características Principales

### Gestión de Tareas
- ✅ Crear, editar, ver y eliminar tareas
- ✅ Asignar prioridades (Alta, Media, Baja)
- ✅ Estados de progreso (Pendiente, En Progreso, Completada)
- ✅ Fechas límite para cada tarea
- ✅ Búsqueda y filtrado avanzado de tareas

### Sistema de Categorías
- 🏷️ Crear y gestionar categorías personalizadas
- 🏷️ Organizar tareas por categorías
- 🏷️ Ver cantidad de tareas por categoría

### Autenticación y Seguridad
- 🔒 Sistema de registro de usuarios
- 🔒 Inicio y cierre de sesión
- 🔒 Cada usuario solo ve y gestiona sus propias tareas
- 🔒 Panel de administración con permisos diferenciados

### Interfaz de Usuario
- 🎨 Diseño responsive con Bootstrap 5
- 🎨 Interfaz intuitiva y moderna
- 🎨 Indicadores visuales de prioridad
- 🎨 Confirmación antes de eliminar elementos

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Base de Datos**: MySQL 8.0
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Icons**: Bootstrap Icons
- **Python**: 3.x

## 📋 Requisitos Previos

Antes de instalar y ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.8 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes de Python)
- Git

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/carandab/Portafolio_Modulo6.git
cd Portafolio_Modulo6
```

### 2. Crear y activar entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django mysqlclient
```

### 4. Configurar la base de datos

1. Crear la base de datos en MySQL:

```sql
CREATE DATABASE taskmanager_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Actualizar las credenciales en `taskmanager/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taskmanager_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 5. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu cuenta de administrador.

### 7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El proyecto estará disponible en: `http://localhost:8000/`

## 📁 Estructura del Proyecto

```
taskmanager_project/
├── manage.py
├── taskmanager/              # Configuración principal del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/                    # Aplicación de gestión de tareas
│   ├── models.py            # Modelos Task y Category
│   ├── views.py             # Vistas de la aplicación
│   ├── forms.py             # Formularios
│   ├── urls.py              # URLs de la app
│   ├── admin.py             # Configuración del admin
│   └── templates/           # Templates HTML
├── users/                    # Aplicación de usuarios
│   ├── views.py             # Vista de registro
│   ├── forms.py             # Formulario de registro
│   ├── urls.py              # URLs de autenticación
│   ├── admin.py             # Admin personalizado de usuarios
│   └── templates/           # Templates de login/registro
├── static/                   # Archivos estáticos
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
└── media/                    # Archivos subidos por usuarios
```

## 🎯 Uso del Sistema

### Para Usuarios Regulares

1. **Registrarse**: Ir a `/users/register/` y crear una cuenta
2. **Iniciar Sesión**: Usar las credenciales creadas
3. **Crear Tareas**: Click en "Nueva Tarea" desde el dashboard
4. **Gestionar Tareas**: Ver, editar o eliminar tareas existentes
5. **Categorías**: Crear categorías para organizar las tareas
6. **Filtros**: Usar los filtros de búsqueda, estado y prioridad

### Para Administradores

1. Acceder al panel de administración: `http://localhost:8000/admin/`
2. Gestionar usuarios y permisos
3. Ver todas las tareas del sistema
4. Configurar categorías globales

## 🔒 Seguridad Implementada

- **Autenticación requerida**: Todas las vistas de tareas requieren login
- **Autorización por usuario**: Los usuarios solo ven sus propias tareas
- **Protección CSRF**: Todos los formularios incluyen tokens CSRF
- **Validación de datos**: Validación en backend de todos los formularios
- **Confirmación de eliminación**: Páginas de confirmación antes de eliminar

## 📊 Modelos de Datos

### Task (Tarea)
- `title`: Título de la tarea
- `description`: Descripción detallada
- `priority`: Prioridad (low, medium, high)
- `status`: Estado (pending, in_progress, completed)
- `category`: Categoría (ForeignKey)
- `user`: Usuario propietario (ForeignKey)
- `due_date`: Fecha límite
- `created_at`: Fecha de creación
- `updated_at`: Última actualización

### Category (Categoría)
- `name`: Nombre de la categoría
- `description`: Descripción opcional
- `created_at`: Fecha de creación

## 🎨 Características de UI/UX

- **Diseño Responsive**: Funciona en móviles, tablets y escritorio
- **Indicadores Visuales**: 
  - Borde de color según prioridad
  - Badges de estado
  - Iconos intuitivos
- **Feedback al Usuario**: Mensajes de éxito/error
- **Confirmaciones**: Diálogos antes de acciones destructivas
- **Animaciones**: Transiciones suaves y efectos hover

## 🔧 Configuración Adicional (Opcional)

### Cambiar idioma a español

En `taskmanager/settings.py`:

```python
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Santiago'
```

### Archivos estáticos en producción

```bash
python manage.py collectstatic
```

## 📝 Requerimientos Funcionales Cumplidos

Este proyecto cumple con todos los requisitos de la evaluación:

✅ **Descripción de Django**: Implementado como framework principal  
✅ **Herramientas administrativas**: Uso de `startproject` y `startapp`  
✅ **Templates dinámicos**: Sistema completo de plantillas  
✅ **Formularios Django**: Forms para tareas y categorías  
✅ **Autenticación**: Sistema completo de login/registro  
✅ **Módulo de administración**: Admin personalizado con permisos  

## 🐛 Solución de Problemas

### Error de conexión a MySQL

- Verifica que MySQL esté corriendo
- Confirma las credenciales en `settings.py`
- Asegúrate de que la base de datos existe

### Error "No module named mysqlclient"

```bash
pip install mysqlclient
```

### Archivos estáticos no se cargan

```bash
python manage.py collectstatic --noinput
```

## 👤 Autor

Desarrollado como proyecto de evaluación de portafolio  
Autor: Cristian Aranda @carandab

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos.


