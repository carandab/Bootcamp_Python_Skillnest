from registros_ORM.models import Producto

productos_data = [
    {"nombre": "Laptop", "precio": 850, "disponible": True},
    {"nombre": "Mouse", "precio": 25, "disponible": True},
    {"nombre": "Teclado", "precio": 45, "disponible": True},
    {"nombre": "Monitor", "precio": 320, "disponible": True},
    {"nombre": "Auriculares", "precio": 65, "disponible": False},
    {"nombre": "Webcam", "precio": 89, "disponible": True},
    {"nombre": "Micrófono", "precio": 120, "disponible": True},
    {"nombre": "Altavoces", "precio": 75, "disponible": False},
    {"nombre": "Tablet", "precio": 450, "disponible": True},
    {"nombre": "Smartphone", "precio": 699, "disponible": True},
    {"nombre": "Cargador", "precio": 15, "disponible": True},
    {"nombre": "Cable USB", "precio": 8, "disponible": True},
    {"nombre": "Disco Duro", "precio": 95, "disponible": True},
    {"nombre": "Memoria RAM", "precio": 125, "disponible": False},
    {"nombre": "Procesador", "precio": 380, "disponible": True},
    {"nombre": "Tarjeta Gráfica", "precio": 550, "disponible": False},
    {"nombre": "Fuente de Poder", "precio": 85, "disponible": True},
    {"nombre": "Gabinete", "precio": 110, "disponible": True},
    {"nombre": "Ventilador", "precio": 30, "disponible": True},
    {"nombre": "Pasta Térmica", "precio": 12, "disponible": True},
    {"nombre": "Mousepad", "precio": 18, "disponible": True},
    {"nombre": "Silla Gamer", "precio": 280, "disponible": False},
    {"nombre": "Escritorio", "precio": 350, "disponible": True},
    {"nombre": "Lámpara LED", "precio": 42, "disponible": True},
    {"nombre": "Router", "precio": 68, "disponible": True},
    {"nombre": "Switch", "precio": 145, "disponible": True},
    {"nombre": "Adaptador WiFi", "precio": 35, "disponible": True},
    {"nombre": "Hub USB", "precio": 28, "disponible": False},
    {"nombre": "Lector de Tarjetas", "precio": 22, "disponible": True},
    {"nombre": "Impresora", "precio": 185, "disponible": True},
    {"nombre": "Scanner", "precio": 210, "disponible": False},
    {"nombre": "Proyector", "precio": 480, "disponible": True},
    {"nombre": "Pizarra Digital", "precio": 920, "disponible": False},
    {"nombre": "Cámara", "precio": 395, "disponible": True},
    {"nombre": "Trípode", "precio": 55, "disponible": True},
    {"nombre": "Estabilizador", "precio": 175, "disponible": True},
    {"nombre": "UPS", "precio": 220, "disponible": True},
    {"nombre": "Batería Externa", "precio": 48, "disponible": True},
    {"nombre": "Audífonos Bluetooth", "precio": 95, "disponible": True},
    {"nombre": "Smartwatch", "precio": 265, "disponible": False},
    {"nombre": "Kindle", "precio": 140, "disponible": True},
    {"nombre": "Apple Watch", "precio": 420, "disponible": True},
    {"nombre": "iPad", "precio": 580, "disponible": True},
    {"nombre": "MacBook", "precio": 999, "disponible": False},
    {"nombre": "iMac", "precio": 950, "disponible": False},
    {"nombre": "AirPods", "precio": 189, "disponible": True},
    {"nombre": "Magic Mouse", "precio": 85, "disponible": True},
    {"nombre": "Magic Keyboard", "precio": 105, "disponible": True},
    {"nombre": "Adaptador HDMI", "precio": 16, "disponible": True},
    {"nombre": "Soporte Laptop", "precio": 38, "disponible": True},
]

productos_creados = []
for data in productos_data:
    producto = Producto(
        nombre=data["nombre"],
        precio=data["precio"],
        disponible=data["disponible"]
    )
    productos_creados.append(producto)

Producto.objects.bulk_create(productos_creados)

print(f"✓ Se crearon {len(productos_creados)} productos exitosamente!")