import os
import django
import random
from decimal import Decimal

""" 
Script para poblar la base de datos con datos de prueba"""

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petshop.settings')
django.setup()

from products.models import Category, Brand, Product

def clear_data():

    print("🗑️  Limpiando datos existentes...")
    Product.objects.all().delete()
    Brand.objects.all().delete()
    Category.objects.all().delete()
    print("✅ Datos limpiados\n")

def create_categories():

    print("📁 Creando categorías...")
    
    categories_data = [
        {
            'name': 'Alimentos',
            'slug': 'alimentos',
            'description': 'Alimentos balanceados y snacks para tu mascota'
        },
        {
            'name': 'Juguetes',
            'slug': 'juguetes',
            'description': 'Juguetes divertidos para entretener a tu mascota'
        },
        {
            'name': 'Cuidado e Higiene',
            'slug': 'cuidado-higiene',
            'description': 'Productos para el cuidado e higiene de tu mascota'
        },
        {
            'name': 'Accesorios',
            'slug': 'accesorios',
            'description': 'Accesorios y complementos para tu mascota'
        },
        {
            'name': 'Farmacia',
            'slug': 'farmacia',
            'description': 'Medicamentos y suplementos veterinarios'
        }
    ]
    
    categories = []
    for cat_data in categories_data:
        category = Category.objects.create(**cat_data)
        categories.append(category)
        print(f"  ✓ {category.name}")
    
    print(f"✅ {len(categories)} categorías creadas\n")
    return categories

def create_brands():

    print("🏷️  Creando marcas...")
    
    brands_data = [
        {'name': 'Pedigree', 'slug': 'pedigree', 'description': 'Alimento para perros de calidad'},
        {'name': 'Whiskas', 'slug': 'whiskas', 'description': 'Alimento premium para gatos'},
        {'name': 'Royal Canin', 'slug': 'royal-canin', 'description': 'Nutrición especializada para mascotas'},
        {'name': 'Dog Chow', 'slug': 'dog-chow', 'description': 'Alimento balanceado para perros'},
        {'name': 'Cat Chow', 'slug': 'cat-chow', 'description': 'Alimento balanceado para gatos'},
        {'name': 'Kong', 'slug': 'kong', 'description': 'Juguetes resistentes para perros'},
        {'name': 'Fancy Pets', 'slug': 'fancy-pets', 'description': 'Accesorios y productos para mascotas'},
        {'name': 'Hartz', 'slug': 'hartz', 'description': 'Productos de cuidado para mascotas'},
        {'name': 'Bravecto', 'slug': 'bravecto', 'description': 'Antiparasitarios de larga duración'},
        {'name': 'Nexgard', 'slug': 'nexgard', 'description': 'Protección contra pulgas y garrapatas'}
    ]
    
    brands = []
    for brand_data in brands_data:
        brand = Brand.objects.create(**brand_data)
        brands.append(brand)
        print(f"  ✓ {brand.name}")
    
    print(f"✅ {len(brands)} marcas creadas\n")
    return brands

def create_products(categories, brands):

    print("📦 Creando productos...")
    
    # Alimentos (15 productos)
    alimentos = [
        {'name': 'Pedigree Adulto Carne 15kg', 'price': 32990, 'stock': 25, 'category': 'Alimentos', 'brand': 'Pedigree'},
        {'name': 'Pedigree Cachorro Pollo 8kg', 'price': 24990, 'stock': 30, 'category': 'Alimentos', 'brand': 'Pedigree'},
        {'name': 'Whiskas Adulto Pescado 10kg', 'price': 28990, 'stock': 20, 'category': 'Alimentos', 'brand': 'Whiskas'},
        {'name': 'Whiskas Gatito Pollo 3kg', 'price': 12990, 'stock': 35, 'category': 'Alimentos', 'brand': 'Whiskas'},
        {'name': 'Royal Canin Mini Adult 7.5kg', 'price': 45990, 'stock': 15, 'category': 'Alimentos', 'brand': 'Royal Canin'},
        {'name': 'Royal Canin Persian Adult 2kg', 'price': 28990, 'stock': 18, 'category': 'Alimentos', 'brand': 'Royal Canin'},
        {'name': 'Dog Chow Adulto Razas Medianas 21kg', 'price': 38990, 'stock': 22, 'category': 'Alimentos', 'brand': 'Dog Chow'},
        {'name': 'Dog Chow Cachorro 8kg', 'price': 22990, 'stock': 28, 'category': 'Alimentos', 'brand': 'Dog Chow'},
        {'name': 'Cat Chow Adulto Carne 8kg', 'price': 24990, 'stock': 25, 'category': 'Alimentos', 'brand': 'Cat Chow'},
        {'name': 'Pedigree Snacks Dentastix 7 unidades', 'price': 3990, 'stock': 50, 'category': 'Alimentos', 'brand': 'Pedigree'},
        {'name': 'Whiskas Snacks Temptations 85g', 'price': 2990, 'stock': 60, 'category': 'Alimentos', 'brand': 'Whiskas'},
        {'name': 'Royal Canin Veterinary Gastro 10kg', 'price': 62990, 'stock': 8, 'category': 'Alimentos', 'brand': 'Royal Canin'},
        {'name': 'Dog Chow Light 7.5kg', 'price': 26990, 'stock': 20, 'category': 'Alimentos', 'brand': 'Dog Chow'},
        {'name': 'Cat Chow Gatito 3kg', 'price': 13990, 'stock': 30, 'category': 'Alimentos', 'brand': 'Cat Chow'},
        {'name': 'Pedigree Adulto Pollo y Arroz 20kg', 'price': 39990, 'stock': 18, 'category': 'Alimentos', 'brand': 'Pedigree'},
    ]
    
    # Juguetes (10 productos)
    juguetes = [
        {'name': 'Kong Classic Rojo Mediano', 'price': 12990, 'stock': 30, 'category': 'Juguetes', 'brand': 'Kong'},
        {'name': 'Kong Extreme Negro Grande', 'price': 18990, 'stock': 20, 'category': 'Juguetes', 'brand': 'Kong'},
        {'name': 'Pelota de Tenis para Perros 3 unidades', 'price': 4990, 'stock': 45, 'category': 'Juguetes', 'brand': 'Fancy Pets'},
        {'name': 'Cuerda para Perro 30cm', 'price': 3990, 'stock': 50, 'category': 'Juguetes', 'brand': 'Fancy Pets'},
        {'name': 'Ratón de Juguete con Catnip', 'price': 2490, 'stock': 60, 'category': 'Juguetes', 'brand': 'Fancy Pets'},
        {'name': 'Varita con Plumas para Gatos', 'price': 3990, 'stock': 40, 'category': 'Juguetes', 'brand': 'Fancy Pets'},
        {'name': 'Kong Wobbler Dispensador de Comida', 'price': 15990, 'stock': 25, 'category': 'Juguetes', 'brand': 'Kong'},
        {'name': 'Frisbee para Perros', 'price': 5990, 'stock': 35, 'category': 'Juguetes', 'brand': 'Fancy Pets'},
        {'name': 'Peluche Pato Chirriador', 'price': 6990, 'stock': 30, 'category': 'Juguetes', 'brand': 'Fancy Pets'},
        {'name': 'Túnel para Gatos Plegable', 'price': 12990, 'stock': 15, 'category': 'Juguetes', 'brand': 'Fancy Pets'},
    ]
    
    # Cuidado e Higiene (10 productos)
    higiene = [
        {'name': 'Shampoo para Perros Antipulgas 500ml', 'price': 8990, 'stock': 35, 'category': 'Cuidado e Higiene', 'brand': 'Hartz'},
        {'name': 'Shampoo para Gatos Hipoalergénico 400ml', 'price': 9990, 'stock': 30, 'category': 'Cuidado e Higiene', 'brand': 'Hartz'},
        {'name': 'Cepillo Deslanador para Perros', 'price': 7990, 'stock': 25, 'category': 'Cuidado e Higiene', 'brand': 'Fancy Pets'},
        {'name': 'Cortauñas para Mascotas Profesional', 'price': 6990, 'stock': 40, 'category': 'Cuidado e Higiene', 'brand': 'Hartz'},
        {'name': 'Toallitas Húmedas para Mascotas 100 unidades', 'price': 5990, 'stock': 45, 'category': 'Cuidado e Higiene', 'brand': 'Hartz'},
        {'name': 'Pasta Dental para Perros Sabor Carne 70g', 'price': 4990, 'stock': 50, 'category': 'Cuidado e Higiene', 'brand': 'Hartz'},
        {'name': 'Cepillo de Dientes para Mascotas', 'price': 3990, 'stock': 55, 'category': 'Cuidado e Higiene', 'brand': 'Fancy Pets'},
        {'name': 'Desodorante Ambiental Anti-Mascotas 500ml', 'price': 6990, 'stock': 30, 'category': 'Cuidado e Higiene', 'brand': 'Hartz'},
        {'name': 'Paños Absorbentes para Entrenamiento 30 unidades', 'price': 12990, 'stock': 25, 'category': 'Cuidado e Higiene', 'brand': 'Fancy Pets'},
        {'name': 'Champú Seco en Espuma 200ml', 'price': 8990, 'stock': 20, 'category': 'Cuidado e Higiene', 'brand': 'Hartz'},
    ]
    
    # Accesorios (10 productos)
    accesorios = [
        {'name': 'Collar Ajustable para Perro Mediano', 'price': 5990, 'stock': 40, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Correa Extensible 5 metros', 'price': 14990, 'stock': 25, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Plato de Acero Inoxidable 1 Litro', 'price': 7990, 'stock': 35, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Bebedero Automático 2 Litros', 'price': 12990, 'stock': 20, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Cama para Mascotas Mediana', 'price': 24990, 'stock': 15, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Transportadora Pequeña', 'price': 19990, 'stock': 18, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Arnés para Perro Talla M', 'price': 9990, 'stock': 30, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Rascador para Gatos 60cm', 'price': 22990, 'stock': 12, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Arenero para Gatos con Tapa', 'price': 16990, 'stock': 20, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
        {'name': 'Chaleco Reflectante para Perros', 'price': 11990, 'stock': 25, 'category': 'Accesorios', 'brand': 'Fancy Pets'},
    ]
    
    # Farmacia (5 productos)
    farmacia = [
        {'name': 'Bravecto Antipulgas Perros 10-20kg', 'price': 32990, 'stock': 15, 'category': 'Farmacia', 'brand': 'Bravecto'},
        {'name': 'Nexgard Antipulgas Perros 4-10kg', 'price': 28990, 'stock': 18, 'category': 'Farmacia', 'brand': 'Nexgard'},
        {'name': 'Desparasitante Interno Perros y Gatos', 'price': 8990, 'stock': 30, 'category': 'Farmacia', 'brand': 'Hartz'},
        {'name': 'Vitaminas para Mascotas 60 tabletas', 'price': 12990, 'stock': 25, 'category': 'Farmacia', 'brand': 'Hartz'},
        {'name': 'Colirio para Limpieza Ocular 50ml', 'price': 6990, 'stock': 35, 'category': 'Farmacia', 'brand': 'Hartz'},
    ]
    
    # Combinar todos los productos
    all_products = alimentos + juguetes + higiene + accesorios + farmacia
    
    # Mapear nombres a objetos
    category_map = {cat.name: cat for cat in categories}
    brand_map = {brand.name: brand for brand in brands}
    
    products = []
    for i, prod_data in enumerate(all_products, 1):
        # Generar SKU
        sku = f"PROD{i:04d}"
        
        # Asignar categoría y marca
        category = category_map.get(prod_data['category'])
        brand = brand_map.get(prod_data['brand'])
        
        # Decidir si tiene precio de oferta (30% de probabilidad)
        sale_price = None
        if random.random() < 0.3:
            discount = random.randint(10, 30)
            sale_price = int(prod_data['price'] * (1 - discount / 100))
        
        # Decidir si es destacado (20% de probabilidad)
        is_featured = random.random() < 0.2
        
        # Crear producto
        product = Product.objects.create(
            name=prod_data['name'],
            sku=sku,
            description=f"Descripción detallada de {prod_data['name']}. Producto de alta calidad para tu mascota.",
            price=prod_data['price'],
            sale_price=sale_price,
            stock=prod_data['stock'],
            category=category,
            brand=brand,
            is_active=True,
            is_featured=is_featured
        )
        
        products.append(product)
        
        # Mostrar progreso
        if i % 10 == 0:
            print(f"  ✓ {i} productos creados...")
    
    print(f"✅ {len(products)} productos creados\n")
    return products

def main():
    print("=" * 60)
    print(" POBLACIÓN DE BASE DE DATOS - GoWest ")
    print("=" * 60)
    print()
    
    # Preguntar si limpiar datos
    response = input("¿Deseas limpiar los datos existentes? (s/n): ").lower()
    if response == 's':
        clear_data()
    
    # Crear datos
    categories = create_categories()
    brands = create_brands()
    products = create_products(categories, brands)
    
    # Resumen
    print("=" * 60)
    print(" RESUMEN ")
    print("=" * 60)
    print(f"✅ Categorías: {Category.objects.count()}")
    print(f"✅ Marcas: {Brand.objects.count()}")
    print(f"✅ Productos: {Product.objects.count()}")
    print(f"   - Con oferta: {Product.objects.filter(sale_price__isnull=False).count()}")
    print(f"   - Destacados: {Product.objects.filter(is_featured=True).count()}")
    print()
    print("✅ Base de datos poblada exitosamente!")
    print("=" * 60)

if __name__ == '__main__':
    main()