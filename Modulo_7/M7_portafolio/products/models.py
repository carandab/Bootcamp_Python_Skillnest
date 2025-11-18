from django.db import models

# Categorías 

class Category(models.Model):

    name = models.CharField(max_length=255) # Nombre de la categoría (ejemplo: "Alimentos para perros")
    description = models.TextField()
    slug = models.SlugField(unique=True)    # URL amigable (ejemplo: "alimentos-para-perros")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name
    
# Marcas

class Brand(models.Model):

    name = models.CharField(max_length=255) # Nombre de la marca (ejemplo: "Pedigree")
    
    logo = models.ImageField(
        upload_to='brands/logos/',
        null=True,
        blank=True,
        verbose_name='Logo')
    
    description = models.TextField()
    slug = models.SlugField(unique=True)    # URL amigable (ejemplo: "pedigree")
    website = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name
    

# Productos

class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name="Nombre")
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(verbose_name="Stock disponible")
    sku = models.CharField(max_length=50, unique=True, verbose_name='SKU')  # Stock Keeping Unit / Código de referencia único

    # Campos temporales
    
    sale_price = models.DecimalField(   # Precio de oferta
        max_digits=10, 
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Precio de oferta'
    )

    is_featured = models.BooleanField(  # Destacado
        default=False,
        verbose_name='Destacado'
    )

    is_active = models.BooleanField(    # Activo
        default=True,
        verbose_name='Activo'
    )


    # Campos de auditoria

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    # Relaciones

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='Categoría',
        related_name='products',

        # Para desarrollo / En producción cambiar a default=funcion o volor por defecto
        blank=True,
        null=True 
        )
    
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Marca',

        # Para desarrollo / En producción cambiar a default=funcion o volor por defecto
        blank=True,
        null=True
        )
    
    # Metadatos
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']


    def __str__(self):
        return self.name
    
