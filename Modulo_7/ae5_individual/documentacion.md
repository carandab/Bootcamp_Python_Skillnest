# Documentación - Ejercicios Django ORM

## Actividad Evaluada: M7_AE5_ABP - Ejercicio Individual

**Proyecto:** ae5_individual  
**Aplicación:** registros_ORM  
**Base de datos:** MySQL (m7_ae5_individual)

---

## Índice

1. [Recuperando Registros con Django ORM](#1-recuperando-registros-con-django-orm)
2. [Aplicando Filtros en Recuperación de Registros](#2-aplicando-filtros-en-recuperación-de-registros)
3. [Ejecutando Queries SQL desde Django](#3-ejecutando-queries-sql-desde-django)
4. [Mapeando Campos de Consultas al Modelo](#4-mapeando-campos-de-consultas-al-modelo)
5. [Realizando Búsquedas de Índice](#5-realizando-búsquedas-de-índice)
6. [Exclusión de Campos del Modelo](#6-exclusión-de-campos-del-modelo)
7. [Añadiendo Anotaciones en Consultas](#7-añadiendo-anotaciones-en-consultas)
8. [Pasando Parámetros a raw()](#8-pasando-parámetros-a-raw)
9. [Ejecutando SQL Personalizado Directamente](#9-ejecutando-sql-personalizado-directamente)
10. [Conexiones y Cursores](#10-conexiones-y-cursores)
11. [Invocación a Procedimientos Almacenados](#11-invocación-a-procedimientos-almacenados)

---

## Modelo Producto

```python
# registros_ORM/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField()
    
    def __str__(self):
        return self.nombre
```

---

## Preparación Inicial

### Acceder a Django Shell

```bash
python manage.py shell
```

### Insertar Datos de Prueba

```python
from registros_ORM.models import Producto

# Crear productos de prueba
Producto.objects.create(nombre="Arroz", precio=45.50, disponible=True)
Producto.objects.create(nombre="Aceite", precio=85.00, disponible=True)
Producto.objects.create(nombre="Azúcar", precio=35.00, disponible=False)
Producto.objects.create(nombre="Frijoles", precio=55.00, disponible=True)
Producto.objects.create(nombre="Leche", precio=25.00, disponible=True)
Producto.objects.create(nombre="Pan", precio=15.00, disponible=True)
Producto.objects.create(nombre="Atún", precio=65.00, disponible=False)
Producto.objects.create(nombre="Agua", precio=20.00, disponible=True)
```

---

## 1. Recuperando Registros con Django ORM

### Objetivo
Utilizar el ORM de Django para recuperar todos los registros de la tabla Producto.

### Comandos

```python
from registros_ORM.models import Producto

# Recuperar todos los registros
productos = Producto.objects.all()

# Mostrar los resultados
for producto in productos:
    print(f"ID: {producto.id} | Nombre: {producto.nombre} | Precio: ${producto.precio} | Disponible: {producto.disponible}")
```

### Resultado Esperado
```
ID: 1 | Nombre: Arroz | Precio: $45.50 | Disponible: True
ID: 2 | Nombre: Aceite | Precio: $85.00 | Disponible: True
ID: 3 | Nombre: Azúcar | Precio: $35.00 | Disponible: False
...
```

### Explicación
- `Producto.objects.all()` recupera todos los registros de la tabla como un QuerySet
- Es el método más básico del ORM de Django
- El QuerySet es lazy (no ejecuta la consulta hasta que se itera)

---

## 2. Aplicando Filtros en Recuperación de Registros

### Objetivo
Utilizar filtros del ORM de Django para consultas específicas.

### 2.1 Productos con precio mayor a 50

```python
from registros_ORM.models import Producto

productos_caros = Producto.objects.filter(precio__gt=50)

print("=== Productos con precio > $50 ===")
for p in productos_caros:
    print(f"{p.nombre}: ${p.precio}")
```

**Resultado esperado:**
```
=== Productos con precio > $50 ===
Aceite: $85.00
Frijoles: $55.00
Atún: $65.00
```

### 2.2 Productos que empiezan con "A"

```python
productos_a = Producto.objects.filter(nombre__startswith='A')

print("\n=== Productos que empiezan con 'A' ===")
for p in productos_a:
    print(f"{p.nombre}")
```

**Resultado esperado:**
```
=== Productos que empiezan con 'A' ===
Arroz
Aceite
Azúcar
Atún
Agua
```

### 2.3 Productos disponibles

```python
productos_disponibles = Producto.objects.filter(disponible=True)

print("\n=== Productos disponibles ===")
for p in productos_disponibles:
    print(f"{p.nombre} - ${p.precio}")
```

**Resultado esperado:**
```
=== Productos disponibles ===
Arroz - $45.50
Aceite - $85.00
Frijoles - $55.00
Leche - $25.00
Pan - $15.00
Agua - $20.00
```

### Explicación de Lookups
- `__gt`: greater than (mayor que)
- `__lt`: less than (menor que)
- `__gte`: greater than or equal (mayor o igual)
- `__lte`: less than or equal (menor o igual)
- `__startswith`: empieza con
- `__endswith`: termina con
- `__contains`: contiene
- `__icontains`: contiene (case insensitive)

---

## 3. Ejecutando Queries SQL desde Django

### Objetivo
Ejecutar consultas SQL directas utilizando el método `raw()`.

### Comandos

```python
from registros_ORM.models import Producto

# Query SQL con raw()
productos_baratos = Producto.objects.raw('SELECT * FROM registros_ORM_producto WHERE precio < 100')

print("=== Productos con precio < $100 (usando raw SQL) ===")
for p in productos_baratos:
    print(f"{p.nombre}: ${p.precio}")
```

### Resultado Esperado
```
=== Productos con precio < $100 (usando raw SQL) ===
Arroz: $45.50
Aceite: $85.00
Azúcar: $35.00
Frijoles: $55.00
Leche: $25.00
Pan: $15.00
Atún: $65.00
Agua: $20.00
```

### Explicación
- `raw()` permite ejecutar SQL directo pero retorna objetos del modelo
- La tabla en MySQL se llama `registros_ORM_producto` (app_modelo en minúsculas)
- Es útil cuando necesitas consultas SQL complejas que el ORM no puede generar fácilmente

---

## 4. Mapeando Campos de Consultas al Modelo

### Objetivo
Ejecutar consultas SQL personalizadas y mapear correctamente los resultados al modelo.

### Comandos

```python
from registros_ORM.models import Producto

# Consulta personalizada con raw()
productos_custom = Producto.objects.raw(
    'SELECT id, nombre, precio, disponible FROM registros_ORM_producto WHERE precio BETWEEN 30 AND 70'
)

print("=== Productos entre $30 y $70 ===")
for p in productos_custom:
    print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: ${p.precio} | Disponible: {p.disponible}")
```

### Resultado Esperado
```
=== Productos entre $30 y $70 ===
ID: 1 | Nombre: Arroz | Precio: $45.50 | Disponible: True
ID: 3 | Nombre: Azúcar | Precio: $35.00 | Disponible: False
ID: 4 | Nombre: Frijoles | Precio: $55.00 | Disponible: True
ID: 7 | Nombre: Atún | Precio: $65.00 | Disponible: False
```

### Explicación del Mapeo
- **Requisito obligatorio:** La consulta SQL DEBE incluir el campo `id` (primary key)
- Los nombres de las columnas en SELECT deben coincidir con los campos del modelo
- Django mapea automáticamente cada columna SQL a su atributo correspondiente en el modelo
- Si falta el `id`, Django lanzará un error

### Ejemplo con Alias

```python
# Usando alias SQL que coinciden con los campos del modelo
productos_alias = Producto.objects.raw(
    '''SELECT 
        id, 
        nombre as nombre, 
        precio * 1.16 as precio, 
        disponible 
       FROM registros_ORM_producto 
       WHERE disponible = 1'''
)

for p in productos_alias:
    print(f"{p.nombre}: ${p.precio} (precio con IVA)")
```

---

## 5. Realizando Búsquedas de Índice

### Objetivo
Comprender qué son los índices en bases de datos y cómo crearlos en Django.

### ¿Qué son los índices?

Los índices en bases de datos son estructuras de datos que mejoran la velocidad de las operaciones de consulta en una tabla. Funcionan como el índice de un libro: permiten encontrar información rápidamente sin tener que revisar toda la tabla.

**Ventajas:**
- Aceleran las búsquedas y filtros
- Mejoran el rendimiento en consultas con WHERE, ORDER BY, JOIN

**Desventajas:**
- Ocupan espacio adicional en disco
- Ralentizan las operaciones INSERT, UPDATE, DELETE

### Modificar el Modelo

Editar `registros_ORM/models.py`:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)  # Índice simple
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField()
    
    class Meta:
        indexes = [
            models.Index(fields=['nombre'], name='idx_nombre'),
            models.Index(fields=['precio'], name='idx_precio'),
            models.Index(fields=['nombre', 'precio'], name='idx_nombre_precio'),  # Índice compuesto
        ]
    
    def __str__(self):
        return self.nombre
```

### Crear y Aplicar Migración

```bash
python manage.py makemigrations
python manage.py migrate
```

### Verificar el Índice en MySQL

```sql
-- Conectarse a MySQL
mysql -u root -p

USE m7_ae5_individual;

-- Ver índices de la tabla
SHOW INDEX FROM registros_ORM_producto;
```

### Probar el Impacto del Índice

```python
from registros_ORM.models import Producto
from django.db import connection
from django.db.models import Q

# Ver el SQL generado
productos = Producto.objects.filter(nombre__startswith='A')
print(productos.query)

# Verificar uso de índices con EXPLAIN
with connection.cursor() as cursor:
    cursor.execute("EXPLAIN SELECT * FROM registros_ORM_producto WHERE nombre LIKE 'A%'")
    for row in cursor.fetchall():
        print(row)
```

### Explicación
- `db_index=True` en el campo crea un índice simple
- `Meta.indexes` permite crear índices más complejos (compuestos, parciales)
- Los índices mejoran significativamente las búsquedas, especialmente en tablas grandes
- Django genera automáticamente el SQL para crear los índices durante la migración

---

## 6. Exclusión de Campos del Modelo

### Objetivo
Recuperar productos omitiendo ciertos campos para optimizar consultas.

### 6.1 Usando defer()

```python
from registros_ORM.models import Producto

# Excluir el campo 'disponible'
productos_sin_disponible = Producto.objects.defer('disponible').all()

print("=== Productos (sin cargar el campo disponible) ===")
for p in productos_sin_disponible:
    print(f"{p.nombre}: ${p.precio}")
    # Si intentamos acceder a p.disponible, Django hará una consulta adicional
```

### 6.2 Usando only()

```python
# Cargar SOLO los campos especificados (más el id)
productos_solo_nombre_precio = Producto.objects.only('nombre', 'precio').all()

print("\n=== Productos (solo nombre y precio) ===")
for p in productos_solo_nombre_precio:
    print(f"{p.nombre}: ${p.precio}")
    # Acceder a p.disponible generaría una consulta adicional
```

### 6.3 Usando values()

```python
# Retorna diccionarios en lugar de objetos del modelo
productos_dict = Producto.objects.values('nombre', 'precio')

print("\n=== Productos como diccionarios ===")
for p in productos_dict:
    print(f"{p['nombre']}: ${p['precio']}")
```

### 6.4 Usando values_list()

```python
# Retorna tuplas
productos_tuplas = Producto.objects.values_list('nombre', 'precio')

print("\n=== Productos como tuplas ===")
for nombre, precio in productos_tuplas:
    print(f"{nombre}: ${precio}")

# Con flat=True (solo un campo)
nombres = Producto.objects.values_list('nombre', flat=True)
print(f"\nNombres: {list(nombres)}")
```

### Explicación de Cada Método

| Método | Retorna | Cuándo usar |
|--------|---------|-------------|
| `defer('campo')` | Objetos del modelo | Excluir campos pesados que no necesitas ahora |
| `only('campo1', 'campo2')` | Objetos del modelo | Solo cargar campos específicos |
| `values('campo1', 'campo2')` | Diccionarios | Cuando no necesitas métodos del modelo |
| `values_list('campo1', 'campo2')` | Tuplas | Máxima eficiencia, datos simples |

### Comparación de SQL Generado

```python
from django.db import connection

# Ver las consultas ejecutadas
from django.db import reset_queries
from django.conf import settings

# Activar el registro de queries (solo en desarrollo)
settings.DEBUG = True

reset_queries()
list(Producto.objects.all())
print(f"all(): {len(connection.queries)} queries")
print(connection.queries[-1]['sql'])

reset_queries()
list(Producto.objects.only('nombre'))
print(f"\nonly('nombre'): {len(connection.queries)} queries")
print(connection.queries[-1]['sql'])
```

---

## 7. Añadiendo Anotaciones en Consultas

### Objetivo
Usar `annotate()` para calcular campos adicionales en las consultas.

### 7.1 Calcular Precio con Impuesto (16%)

```python
from registros_ORM.models import Producto
from django.db.models import F, ExpressionWrapper, DecimalField

# Calcular precio con impuesto del 16%
productos_con_impuesto = Producto.objects.annotate(
    precio_con_impuesto=ExpressionWrapper(
        F('precio') * 1.16,
        output_field=DecimalField(max_digits=10, decimal_places=2)
    )
)

print("=== Productos con impuesto del 16% ===")
for p in productos_con_impuesto:
    print(f"{p.nombre}:")
    print(f"  Precio base: ${p.precio}")
    print(f"  Con impuesto: ${p.precio_con_impuesto}")
    print(f"  Impuesto: ${p.precio_con_impuesto - p.precio}\n")
```

### 7.2 Más Ejemplos de Anotaciones

```python
from django.db.models import Count, Avg, Max, Min, Sum, Q, Case, When, Value, CharField

# Ejemplo: Categorizar productos por precio
productos_categorizados = Producto.objects.annotate(
    categoria=Case(
        When(precio__lt=30, then=Value('Económico')),
        When(precio__lt=60, then=Value('Medio')),
        default=Value('Premium'),
        output_field=CharField()
    )
)

print("\n=== Productos categorizados por precio ===")
for p in productos_categorizados:
    print(f"{p.nombre} (${p.precio}): {p.categoria}")
```

### 7.3 Anotaciones con Agregaciones

```python
from django.db.models import Avg, Max, Min, Count

# Estadísticas generales
estadisticas = Producto.objects.aggregate(
    precio_promedio=Avg('precio'),
    precio_maximo=Max('precio'),
    precio_minimo=Min('precio'),
    total_productos=Count('id'),
    total_disponibles=Count('id', filter=Q(disponible=True))
)

print("\n=== Estadísticas de Productos ===")
print(f"Precio promedio: ${estadisticas['precio_promedio']:.2f}")
print(f"Precio máximo: ${estadisticas['precio_maximo']}")
print(f"Precio mínimo: ${estadisticas['precio_minimo']}")
print(f"Total productos: {estadisticas['total_productos']}")
print(f"Productos disponibles: {estadisticas['total_disponibles']}")
```

### Explicación
- `annotate()` añade campos calculados a cada objeto del QuerySet
- `aggregate()` calcula valores sobre todo el QuerySet (retorna un diccionario)
- `F()` referencia campos del modelo en la consulta
- `ExpressionWrapper()` permite especificar el tipo de dato del resultado
- `Case/When` permite crear lógica condicional en la base de datos

---

## 8. Pasando Parámetros a raw()

### Objetivo
Entender la diferencia entre consultas con valores fijos y con parámetros, y los beneficios de seguridad.

### 8.1 Forma INCORRECTA (Vulnerable a SQL Injection)

```python
from registros_ORM.models import Producto

# ⚠️ NUNCA HACER ESTO - Vulnerable a SQL Injection
precio_limite = 50
productos_inseguro = Producto.objects.raw(
    f'SELECT * FROM registros_ORM_producto WHERE precio > {precio_limite}'
)

print("=== Forma INSEGURA (NO USAR) ===")
for p in productos_inseguro:
    print(f"{p.nombre}: ${p.precio}")
```

**¿Por qué es peligroso?**
```python
# Un atacante podría inyectar código SQL malicioso
precio_limite = "0 OR 1=1; DROP TABLE registros_ORM_producto; --"
# Esto podría eliminar toda la tabla
```

### 8.2 Forma CORRECTA (Usando Parámetros)

```python
# ✅ FORMA SEGURA - Usando parámetros
precio_limite = 50
productos_seguro = Producto.objects.raw(
    'SELECT * FROM registros_ORM_producto WHERE precio > %s',
    [precio_limite]
)

print("\n=== Forma SEGURA (usar parámetros) ===")
for p in productos_seguro:
    print(f"{p.nombre}: ${p.precio}")
```

### 8.3 Múltiples Parámetros

```python
# Con múltiples parámetros
precio_min = 30
precio_max = 70
letra_inicial = 'A'

productos_parametrizados = Producto.objects.raw(
    '''SELECT * FROM registros_ORM_producto 
       WHERE precio BETWEEN %s AND %s 
       AND nombre LIKE %s''',
    [precio_min, precio_max, f'{letra_inicial}%']
)

print("\n=== Consulta con múltiples parámetros ===")
for p in productos_parametrizados:
    print(f"{p.nombre}: ${p.precio}")
```

### 8.4 Usando Parámetros Nombrados (Diccionario)

```python
# Con parámetros nombrados
productos_nombrados = Producto.objects.raw(
    '''SELECT * FROM registros_ORM_producto 
       WHERE precio > %(precio)s 
       AND disponible = %(disponible)s''',
    {'precio': 40, 'disponible': True}
)

print("\n=== Consulta con parámetros nombrados ===")
for p in productos_nombrados:
    print(f"{p.nombre}: ${p.precio} - Disponible: {p.disponible}")
```

### Beneficios de Usar Parámetros

1. **Seguridad:** Previene inyección SQL
2. **Escapado automático:** Django escapa los valores correctamente
3. **Reutilización:** El mismo query puede usarse con diferentes valores
4. **Rendimiento:** Algunos motores de BD pueden cachear el plan de ejecución
5. **Legibilidad:** El código es más claro y mantenible

### Comparación

```python
# Ver el SQL real generado
import logging
logging.basicConfig()
logging.getLogger('django.db.backends').setLevel(logging.DEBUG)

# Ahora ejecuta las consultas y verás el SQL real en la consola
productos = Producto.objects.raw('SELECT * FROM registros_ORM_producto WHERE precio > %s', [50])
list(productos)
```

---

## 9. Ejecutando SQL Personalizado Directamente

### Objetivo
Usar `connection.cursor()` para ejecutar SQL directo (INSERT, UPDATE, DELETE) sin pasar por el ORM.

### 9.1 INSERT

```python
from django.db import connection

# Insertar un nuevo producto
with connection.cursor() as cursor:
    cursor.execute(
        "INSERT INTO registros_ORM_producto (nombre, precio, disponible) VALUES (%s, %s, %s)",
        ['Café', 120.00, True]
    )
    producto_id = cursor.lastrowid
    print(f"✓ Producto insertado con ID: {producto_id}")
```

### 9.2 UPDATE

```python
# Actualizar el precio del café
with connection.cursor() as cursor:
    cursor.execute(
        "UPDATE registros_ORM_producto SET precio = %s WHERE nombre = %s",
        [130.00, 'Café']
    )
    filas_afectadas = cursor.rowcount
    print(f"✓ {filas_afectadas} producto(s) actualizado(s)")
```

### 9.3 DELETE

```python
# Eliminar productos no disponibles con precio bajo
with connection.cursor() as cursor:
    cursor.execute(
        "DELETE FROM registros_ORM_producto WHERE disponible = %s AND precio < %s",
        [False, 40]
    )
    filas_eliminadas = cursor.rowcount
    print(f"✓ {filas_eliminadas} producto(s) eliminado(s)")
```

### 9.4 SELECT Complejo

```python
# Consulta compleja con JOIN (si tuviéramos tablas relacionadas)
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT 
            nombre,
            precio,
            CASE 
                WHEN disponible = 1 THEN 'Sí'
                ELSE 'No'
            END as disponibilidad,
            precio * 1.16 as precio_con_iva
        FROM registros_ORM_producto
        WHERE precio > %s
        ORDER BY precio DESC
    """, [50])
    
    print("\n=== Productos > $50 con IVA ===")
    print(f"{'Nombre':<15} {'Precio':<10} {'Disponible':<12} {'Con IVA':<10}")
    print("-" * 50)
    
    for row in cursor.fetchall():
        nombre, precio, disponible, precio_iva = row
        print(f"{nombre:<15} ${precio:<9.2f} {disponible:<12} ${precio_iva:<9.2f}")
```

### 9.5 Transacciones

```python
from django.db import connection, transaction

# Usar transacciones para garantizar consistencia
try:
    with transaction.atomic():
        with connection.cursor() as cursor:
            # Aumentar todos los precios un 10%
            cursor.execute("UPDATE registros_ORM_producto SET precio = precio * 1.10")
            
            # Insertar un registro de auditoría (ejemplo)
            cursor.execute(
                "INSERT INTO registros_ORM_producto (nombre, precio, disponible) VALUES (%s, %s, %s)",
                ['Producto Temporal', 99.99, True]
            )
            
            print("✓ Transacción completada exitosamente")
            
except Exception as e:
    print(f"✗ Error en la transacción: {e}")
    print("  (Todos los cambios fueron revertidos)")
```

### Cuándo Usar connection.cursor()

**✅ Usar cuando:**
- Necesitas ejecutar SQL muy complejo que el ORM no puede generar
- Operaciones masivas que son más eficientes en SQL puro
- Trabajas con funciones específicas de la base de datos
- Necesitas ejecutar procedimientos almacenados complejos
- Optimizaciones de rendimiento críticas

**❌ Evitar cuando:**
- Las operaciones pueden hacerse con el ORM (más seguro y portable)
- Estás haciendo CRUD simple
- Necesitas portabilidad entre diferentes bases de datos
- El código debe ser mantenido por otros desarrolladores

### Comparación ORM vs SQL Directo

```python
from django.db import connection
from registros_ORM.models import Producto
import time

# Insertar 1000 productos con ORM
inicio = time.time()
for i in range(1000):
    Producto.objects.create(
        nombre=f"Producto {i}",
        precio=10.00 + i,
        disponible=True
    )
fin = time.time()
print(f"ORM: {fin - inicio:.2f} segundos")

# Insertar 1000 productos con SQL directo
inicio = time.time()
with connection.cursor() as cursor:
    for i in range(1000, 2000):
        cursor.execute(
            "INSERT INTO registros_ORM_producto (nombre, precio, disponible) VALUES (%s, %s, %s)",
            [f"Producto {i}", 10.00 + i, True]
        )
fin = time.time()
print(f"SQL directo: {fin - inicio:.2f} segundos")

# Limpiar
Producto.objects.filter(nombre__startswith='Producto').delete()
```

---

## 10. Conexiones y Cursores

### Objetivo
Crear conexiones manuales a la base de datos y usar cursores para recuperar datos.

### 10.1 Recuperar Datos con Cursor

```python
from django.db import connection

# Crear conexión y recuperar datos
with connection.cursor() as cursor:
    cursor.execute("SELECT id, nombre, precio, disponible FROM registros_ORM_producto")
    
    print("=== Datos recuperados con cursor ===")
    print(f"{'ID':<5} {'Nombre':<15} {'Precio':<10} {'Disponible'}")
    print("-" * 45)
    
    # Opción 1: fetchall() - recupera todos los registros
    rows = cursor.fetchall()
    for row in rows:
        disponible = "Sí" if row[3] else "No"
        print(f"{row[0]:<5} {row[1]:<15} ${row[2]:<9.2f} {disponible}")
```

### 10.2 fetchone() - Recuperar Registro por Registro

```python
with connection.cursor() as cursor:
    cursor.execute("SELECT nombre, precio FROM registros_ORM_producto WHERE disponible = %s", [True])
    
    print("\n=== Usando fetchone() ===")
    row = cursor.fetchone()
    contador = 0
    while row:
        contador += 1
        print(f"{contador}. {row[0]}: ${row[1]}")
        row = cursor.fetchone()
```

### 10.3 fetchmany() - Recuperar en Lotes

```python
with connection.cursor() as cursor:
    cursor.execute("SELECT nombre, precio FROM registros_ORM_producto ORDER BY precio DESC")
    
    print("\n=== Usando fetchmany(3) - en lotes de 3 ===")
    lote = 1
    while True:
        rows = cursor.fetchmany(3)
        if not rows:
            break
        
        print(f"\nLote {lote}:")
        for row in rows:
            print(f"  {row[0]}: ${row[1]}")
        lote += 1
```

### 10.4 Cursor como Diccionario

```python
from django.db import connection

# Usar DictCursor para obtener resultados como diccionarios
with connection.cursor() as cursor:
    cursor.execute("SELECT id, nombre, precio, disponible FROM registros_ORM_producto LIMIT 5")
    
    # Obtener nombres de columnas
    columns = [col[0] for col in cursor.description]
    
    print("\n=== Cursor como diccionarios ===")
    for row in cursor.fetchall():
        # Convertir tupla a diccionario
        producto_dict = dict(zip(columns, row))
        print(producto_dict)
```

### 10.5 Información del Cursor

```python
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM registros_ORM_producto")
    
    print("\n=== Información del Cursor ===")
    print(f"Columnas: {[desc[0] for desc in cursor.description]}")
    print(f"Número de filas: {cursor.rowcount}")
    
    # Tipos de datos de cada columna
    print("\nTipos de datos:")
    for col in cursor.description:
        print(f"  {col[0]}: {col[1]}")
```

### 10.6 Múltiples Consultas

```python
with connection.cursor() as cursor:
    # Primera consulta
    cursor.execute("SELECT COUNT(*) FROM registros_ORM_producto")
    total = cursor.fetchone()[0]
    
    # Segunda consulta
    cursor.execute("SELECT COUNT(*) FROM registros_ORM_producto WHERE disponible = 1")
    disponibles = cursor.fetchone()[0]
    
    # Tercera consulta
    cursor.execute("SELECT AVG(precio) FROM registros_ORM_producto")
    promedio = cursor.fetchone()[0]
    
    print(f"\n=== Estadísticas ===")
    print(f"Total de productos: {total}")
    print(f"Productos disponibles: {disponibles}")
    print(f"Precio promedio: ${promedio:.2f}")
```

### Ventajas y Desventajas

#### ✅ VENTAJAS del Cursor

1. **Control total:** Acceso directo a funcionalidades de la base de datos
2. **Rendimiento:** Para operaciones muy específicas puede ser más rápido
3. **Flexibilidad:** Puedes ejecutar cualquier SQL válido
4. **Memoria:** Con `fetchmany()` puedes procesar grandes cantidades de datos sin cargar todo en memoria
5. **Funciones nativas:** Acceso completo a funciones y características específicas de la BD

#### ❌ DESVENTAJAS del Cursor

1. **Portabilidad:** El código SQL puede no funcionar en otras bases de datos
2. **Seguridad:** Mayor riesgo si no se usan parámetros correctamente
3. **Mantenibilidad:** Más difícil de leer y mantener
4. **Sin validaciones:** No hay validaciones del modelo
5. **Sin caché:** No se beneficia del sistema de caché del ORM
6. **Verbose:** Requiere más código que el ORM
7. **Sin relaciones:** Debes manejar manualmente las relaciones entre tablas

#### 📊 COMPARACIÓN

```python
from registros_ORM.models import Producto
from django.db import connection

# Con ORM
productos_orm = Producto.objects.filter(precio__gt=50).order_by('-precio')
for p in productos_orm:
    print(f"{p.nombre}: ${p.precio}")

# Con Cursor
with connection.cursor() as cursor:
    cursor.execute(
        "SELECT nombre, precio FROM registros_ORM_producto WHERE precio > %s ORDER BY precio DESC",
        [50]
    )
    for row in cursor.fetchall():
        print(f"{row[0]}: ${row[1]}")
```

### Recomendación

**Usa el ORM** para el 95% de tus operaciones. Solo usa cursores cuando:
- Realmente necesites optimización extrema
- Estés ejecutando SQL muy complejo
- Trabajes con procedimientos almacenados
- Necesites funciones específicas de tu base de datos

---

## 11. Invocación a Procedimientos Almacenados

### Objetivo
Comprender qué son los procedimientos almacenados y cómo invocarlos desde Django.

### ¿Qué son los Procedimientos Almacenados?

Los **procedimientos almacenados** (stored procedures) son conjuntos de instrucciones SQL que se almacenan en el servidor de base de datos y pueden ser ejecutados mediante una simple llamada.

**Ventajas:**
- Lógica de negocio centralizada en la BD
- Mejor rendimiento (código precompilado)
- Reducción del tráfico de red
- Reutilización de código
- Mayor seguridad (control de acceso granular)

**Desventajas:**
- Menor portabilidad entre diferentes SGBD
- Más difícil de versionar y testear
- Mezcla lógica de negocio con la capa de datos

### 11.1 Crear Procedimientos Almacenados en MySQL

Ejecuta esto directamente en MySQL:

```sql
USE m7_ae5_individual;

-- Procedimiento 1: Obtener productos por precio mínimo
DELIMITER //

CREATE PROCEDURE obtener_productos_por_precio(IN precio_minimo DECIMAL(5,2))
BEGIN
    SELECT * FROM registros_ORM_producto 
    WHERE precio >= precio_minimo
    ORDER BY precio ASC;
END //

DELIMITER ;


-- Procedimiento 2: Obtener estadísticas de productos
DELIMITER //

CREATE PROCEDURE estadisticas_productos()
BEGIN
    SELECT 
        COUNT(*) as total_productos,
        SUM(CASE WHEN disponible = 1 THEN 1 ELSE 0 END) as total_disponibles,
        AVG(precio) as precio_promedio,
        MIN(precio) as precio_minimo,
        MAX(precio) as precio_maximo
    FROM registros_ORM_producto;
END //

DELIMITER ;


-- Procedimiento 3: Actualizar precio con porcentaje
DELIMITER //

CREATE PROCEDURE actualizar_precios(
    IN porcentaje DECIMAL(5,2),
    IN solo_disponibles BOOLEAN
)
BEGIN
    IF solo_disponibles THEN
        UPDATE registros_ORM_producto 
        SET precio = precio * (1 + porcentaje / 100)
        WHERE disponible = 1;
    ELSE
        UPDATE registros_ORM_producto 
        SET precio = precio * (1 + porcentaje / 100);
    END IF;
    
    SELECT ROW_COUNT() as filas_actualizadas;
END //

DELIMITER ;


-- Procedimiento 4: Búsqueda flexible
DELIMITER //

CREATE PROCEDURE buscar_productos(
    IN termino_busqueda VARCHAR(100),
    IN precio_max DECIMAL(5,2)
)
BEGIN
    SELECT * FROM registros_ORM_producto
    WHERE nombre LIKE CONCAT('%', termino_busqueda, '%')
    AND precio <= precio_max
    ORDER BY nombre;
END //

DELIMITER ;
```

### 11.2 Invocar Procedimientos desde Django

```python
from django.db import connection

# Procedimiento 1: Obtener productos por precio mínimo
print("=== Procedimiento: obtener_productos_por_precio ===")
with connection.cursor() as cursor:
    cursor.callproc('obtener_productos_por_precio', [50.00])
    
    # Obtener los resultados
    resultados = cursor.fetchall()
    
    print(f"{'ID':<5} {'Nombre':<15} {'Precio':<10} {'Disponible'}")
    print("-" * 45)
    for row in resultados:
        disponible = "Sí" if row[3] else "No"
        print(f"{row[0]:<5} {row[1]:<15} ${row[2]:<9.2f} {disponible}")
```

### 11.3 Procedimiento sin Parámetros

```python
# Procedimiento 2: Estadísticas
print("\n=== Procedimiento: estadisticas_productos ===")
with connection.cursor() as cursor:
    cursor.callproc('estadisticas_productos')
    
    resultado = cursor.fetchone()
    
    print(f"Total de productos: {resultado[0]}")
    print(f"Productos disponibles: {resultado[1]}")
    print(f"Precio promedio: ${resultado[2]:.2f}")
    print(f"Precio mínimo: ${resultado[3]:.2f}")
    print(f"Precio máximo: ${resultado[4]:.2f}")
```

### 11.4 Procedimiento con Múltiples Parámetros

```python
# Procedimiento 3: Actualizar precios
print("\n=== Procedimiento: actualizar_precios ===")
with connection.cursor() as cursor:
    # Aumentar precios un 5% solo en productos disponibles
    cursor.callproc('actualizar_precios', [5.0, True])
    
    # Obtener el resultado (filas actualizadas)
    resultado = cursor.fetchone()
    print(f"Filas actualizadas: {resultado[0]}")
```

### 11.5 Procedimiento de Búsqueda

```python
# Procedimiento 4: Búsqueda flexible
print("\n=== Procedimiento: buscar_productos ===")
with connection.cursor() as cursor:
    cursor.callproc('buscar_productos', ['a', 100.00])
    
    resultados = cursor.fetchall()
    
    print(f"Productos que contienen 'a' y cuestan menos de $100:")
    for row in resultados:
        print(f"  {row[1]}: ${row[2]}")
```

### 11.6 Manejo de Errores

```python
from django.db import connection
from django.db.utils import DatabaseError

print("\n=== Manejo de errores en procedimientos ===")
try:
    with connection.cursor() as cursor:
        cursor.callproc('procedimiento_inexistente', [])
        
except DatabaseError as e:
    print(f"Error al ejecutar el procedimiento: {e}")
```

### 11.7 Procedimiento con OUT Parameters

```sql
-- Crear procedimiento con parámetros OUT
DELIMITER //

CREATE PROCEDURE contar_por_disponibilidad(
    OUT total INT,
    OUT disponibles INT,
    OUT no_disponibles INT
)
BEGIN
    SELECT COUNT(*) INTO total FROM registros_ORM_producto;
    SELECT COUNT(*) INTO disponibles FROM registros_ORM_producto WHERE disponible = 1;
    SELECT COUNT(*) INTO no_disponibles FROM registros_ORM_producto WHERE disponible = 0;
END //

DELIMITER ;
```

```python
# Invocar procedimiento con OUT parameters
print("\n=== Procedimiento con OUT parameters ===")
with connection.cursor() as cursor:
    # Ejecutar el procedimiento
    cursor.execute("CALL contar_por_disponibilidad(@total, @disponibles, @no_disponibles)")
    
    # Recuperar los valores OUT
    cursor.execute("SELECT @total, @disponibles, @no_disponibles")
    resultado = cursor.fetchone()
    
    print(f"Total: {resultado[0]}")
    print(f"Disponibles: {resultado[1]}")
    print(f"No disponibles: {resultado[2]}")
```

### Verificar Procedimientos Almacenados Existentes

```sql
-- En MySQL
SHOW PROCEDURE STATUS WHERE Db = 'm7_ae5_individual';

-- Ver el código de un procedimiento
SHOW CREATE PROCEDURE obtener_productos_por_precio;
```

### Eliminar Procedimientos

```sql
-- Si necesitas recrear o eliminar un procedimiento
DROP PROCEDURE IF EXISTS obtener_productos_por_precio;
DROP PROCEDURE IF EXISTS estadisticas_productos;
DROP PROCEDURE IF EXISTS actualizar_precios;
DROP PROCEDURE IF EXISTS buscar_productos;
DROP PROCEDURE IF EXISTS contar_por_disponibilidad;
```

### Cuándo Usar Procedimientos Almacenados

**✅ Usar cuando:**
- Tienes lógica compleja que se ejecuta frecuentemente
- Necesitas optimización extrema de rendimiento
- Varios sistemas/aplicaciones acceden a la misma base de datos
- Requieres transacciones complejas
- Necesitas control de acceso granular

**❌ Evitar cuando:**
- La lógica de negocio debe estar en la aplicación
- Necesitas portabilidad entre diferentes SGBD
- El equipo no tiene experiencia con SQL avanzado
- Prefieres testing y debugging en código Python

### Ejemplo Completo de Uso

```python
from django.db import connection

def reporte_productos():
    """
    Genera un reporte completo usando procedimientos almacenados
    """
    print("=" * 60)
    print("REPORTE DE PRODUCTOS".center(60))
    print("=" * 60)
    
    with connection.cursor() as cursor:
        # Estadísticas generales
        cursor.callproc('estadisticas_productos')
        stats = cursor.fetchone()
        
        print(f"\n📊 ESTADÍSTICAS GENERALES")
        print(f"   Total de productos: {stats[0]}")
        print(f"   Productos disponibles: {stats[1]}")
        print(f"   Precio promedio: ${stats[2]:.2f}")
        print(f"   Rango de precios: ${stats[3]:.2f} - ${stats[4]:.2f}")
        
        # Productos premium (>$50)
        print(f"\n💎 PRODUCTOS PREMIUM (precio > $50)")
        cursor.callproc('obtener_productos_por_precio', [50.00])
        productos_premium = cursor.fetchall()
        
        for prod in productos_premium:
            print(f"   • {prod[1]}: ${prod[2]}")
        
        # Búsqueda
        print(f"\n🔍 BÚSQUEDA: Productos con 'a' hasta $100")
        cursor.callproc('buscar_productos', ['a', 100.00])
        productos_busqueda = cursor.fetchall()
        
        for prod in productos_busqueda:
            print(f"   • {prod[1]}: ${prod[2]}")
    
    print("\n" + "=" * 60)

# Ejecutar el reporte
reporte_productos()
```

---

## Resumen de Comandos Principales

```python
# Importaciones necesarias
from registros_ORM.models import Producto
from django.db import connection
from django.db.models import F, Q, Count, Avg, Max, Min, Sum
from django.db.models import ExpressionWrapper, DecimalField, CharField, Case, When, Value

# 1. ORM Básico
Producto.objects.all()
Producto.objects.filter(precio__gt=50)
Producto.objects.exclude(disponible=False)
Producto.objects.get(id=1)

# 2. Queries avanzadas
Producto.objects.filter(precio__range=(30, 70))
Producto.objects.filter(nombre__icontains='a')
Producto.objects.order_by('-precio')

# 3. Raw SQL
Producto.objects.raw('SELECT * FROM registros_ORM_producto WHERE precio < %s', [100])

# 4. Optimización
Producto.objects.defer('disponible')
Producto.objects.only('nombre', 'precio')
Producto.objects.values('nombre', 'precio')
Producto.objects.values_list('nombre', flat=True)

# 5. Anotaciones
Producto.objects.annotate(precio_con_impuesto=F('precio') * 1.16)

# 6. Agregaciones
Producto.objects.aggregate(precio_promedio=Avg('precio'))

# 7. Cursor directo
with connection.cursor() as cursor:
    cursor.execute('SELECT * FROM registros_ORM_producto')
    rows = cursor.fetchall()

# 8. Procedimientos almacenados
with connection.cursor() as cursor:
    cursor.callproc('obtener_productos_por_precio', [50.00])
    results = cursor.fetchall()
```

---

## Comandos de Gestión

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Abrir shell de Django
python manage.py shell

# Ver SQL de las migraciones
python manage.py sqlmigrate registros_ORM 0001

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

---

## Notas Finales

### Mejores Prácticas

1. **Usa el ORM siempre que sea posible** - Es más seguro y mantenible
2. **Parámetriza las consultas SQL** - Previene inyección SQL
3. **Usa índices estratégicamente** - Solo en campos que se consultan frecuentemente
4. **Optimiza con select_related() y prefetch_related()** - Para relaciones
5. **Usa defer() y only() con cuidado** - Pueden generar más consultas si no se usan bien
6. **Documenta el código SQL complejo** - Será difícil de entender después
7. **Testea el rendimiento** - Usa django-debug-toolbar en desarrollo
8. **Usa transacciones** - Para operaciones que deben ser atómicas

### Seguridad

- ✅ SIEMPRE usa parámetros en raw() y cursor.execute()
- ❌ NUNCA concatenes strings para formar SQL
- ✅ Valida y sanitiza las entradas de usuario
- ✅ Usa el ORM cuando sea posible (maneja escape automáticamente)
- ✅ Implementa permisos y autenticación adecuados

### Rendimiento

- Usa `select_related()` para Foreign Keys (JOIN)
- Usa `prefetch_related()` para Many-to-Many
- Implementa caché para consultas frecuentes
- Usa `iterator()` para procesar grandes cantidades de datos
- Analiza queries lentas con `EXPLAIN` en MySQL
- Considera usar índices compuestos para consultas comunes

---

## Recursos Adicionales

- [Documentación oficial de Django ORM](https://docs.djangoproject.com/en/stable/topics/db/)
- [Django QuerySet API](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [Optimización de base de datos en Django](https://docs.djangoproject.com/en/stable/topics/db/optimization/)
- [SQL en Django](https://docs.djangoproject.com/en/stable/topics/db/sql/)

---

**Fecha de creación:** Noviembre 2025  
**Autor:** Cristian Aranda  
**Proyecto:** ae5_individual  
**Curso:** BOTIC-SOFOF-24-28-13-0076 Bootcamp Full Stack Python Skillnest para Talento Digital