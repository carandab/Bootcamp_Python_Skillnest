from django import template

register = template.Library()


# Formatea un valor numérico como precio en pesos chilenos (CLP)

@register.filter(name='precio_clp')
def precio_clp(value):

    try:
        # Convertir a entero
        value = int(value)
        # Formatear con separador de miles
        return f"${value:,}".replace(',', '.')
    except (ValueError, TypeError):
        return value
    
# Calcular descuento
@register.filter(name='calcular_descuento')
def calcular_descuento(precio_normal, precio_oferta):
    """
    Calcula el porcentaje de descuento
    """
    try:
        precio_normal = float(precio_normal)
        precio_oferta = float(precio_oferta)
        
        if precio_normal > 0:
            descuento = ((precio_normal - precio_oferta) / precio_normal) * 100
            return int(descuento)
        return 0
    except (ValueError, TypeError, ZeroDivisionError):
        return 0