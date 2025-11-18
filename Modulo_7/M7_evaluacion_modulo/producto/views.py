from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto, DetallesProducto, ProductoEtiqueta
from .forms import ProductoForm, DetallesProductoForm, ProductoEtiquetaFormSet
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from django.db.models import Q

def index(request):

    context = {
        'total_productos': Producto.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'total_etiquetas': Etiqueta.objects.count(),
    }

    return render(request, 'index.html', context)


def lista_productos(request):

    productos = Producto.objects.select_related('categoria').prefetch_related('etiquetas')
    
    # Filtros
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')
    precio_min = request.GET.get('precio_min')
    
    categorias = Categoria.objects.all()

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
    
    return render(request, 'producto/lista.html', {
        'productos': productos,
        'categorias': categorias
    })


def detalle_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto/detalle.html', {'producto': producto})


def crear_producto(request):

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        detalles_form = DetallesProductoForm(request.POST)
        
        if producto_form.is_valid() and detalles_form.is_valid():
            
            # Guardar el Producto primero (para obtener su ID)
            producto = producto_form.save()
            
            # - Guardar Detalles solo si hay datos
            # - Verifica si al menos uno de los campos tiene valor

            if detalles_form.cleaned_data.get('peso') or detalles_form.cleaned_data.get('dimensiones'): 

                detalles = detalles_form.save(commit=False)  # No guardar ahora
                detalles.producto = producto  # Asignar el producto recién creado
                detalles.save()  # Guardar los detalles
            
            # Guardar Etiquetas usando through 

            etiquetas_seleccionadas = producto_form.cleaned_data.get('etiquetas_seleccionadas')

            if etiquetas_seleccionadas:
                for orden, etiqueta in enumerate(etiquetas_seleccionadas, start=1):
                    ProductoEtiqueta.objects.create(
                        producto=producto,
                        etiqueta=etiqueta,
                        orden=orden
                    )
            
            messages.success(request, 'Producto creado exitosamente')
            return redirect('detalle_producto', id=producto.id)
        
        else:
            # Mensaje de errores
            messages.error(request, 'Por favor corrige los errores del formulario')
    else:
        producto_form = ProductoForm()
        detalles_form = DetallesProductoForm()
    
    return render(request, 'producto/crear.html', {
        'producto_form': producto_form,
        'detalles_form': detalles_form
    })


def editar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    # Manejo de excepciones para obtener detalles si existen

    try:
        detalles = producto.detalles

    except DetallesProducto.DoesNotExist:   # Si detalles no existen, asignar None
        detalles = None
    
    if request.method == 'POST':

        producto_form = ProductoForm(request.POST, instance=producto)
        
        # Formulario de detalles (existente o nuevo)
        if detalles:
            detalles_form = DetallesProductoForm(request.POST, instance=detalles)
        else:
            detalles_form = DetallesProductoForm(request.POST)
        
        # Formset de etiquetas
        etiquetas_formset = ProductoEtiquetaFormSet(request.POST, instance=producto)
        
        if producto_form.is_valid() and detalles_form.is_valid() and etiquetas_formset.is_valid():
            
            # Guardar producto
            producto_form.save()
            
            # Guardar o crear detalles SOLO si hay datos
            if detalles_form.cleaned_data.get('peso') or detalles_form.cleaned_data.get('dimensiones'):

                if not detalles:

                    # Crear nuevos detalles si no existen

                    detalles = detalles_form.save(commit=False)
                    detalles.producto = producto
                    detalles.save()

                else:

                    # Actualizar detalles existentes
                    detalles_form.save()

            elif detalles:

                # Si ya existían detalles pero ahora están vacíos, eliminarlos

                if not detalles_form.cleaned_data.get('peso') and not detalles_form.cleaned_data.get('dimensiones'):
                    detalles.delete()
            
            # Guardar etiquetas
            etiquetas_formset.save()
            
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('detalle_producto', id=producto.id)
        

        else:
            messages.error(request, 'Por favor corrige los errores del formulario') # Mensaje de errores

    else:
        producto_form = ProductoForm(instance=producto)
        detalles_form = DetallesProductoForm(instance=detalles) if detalles else DetallesProductoForm()
        etiquetas_formset = ProductoEtiquetaFormSet(instance=producto)
    
    return render(request, 'producto/editar.html', {
        'producto': producto,
        'producto_form': producto_form,
        'detalles_form': detalles_form,
        'etiquetas_formset': etiquetas_formset
    })



def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':

        nombre_producto = producto.nombre
        producto.delete()  # Esto también eliminará DetallesProducto por CASCADE definida en modelo
        messages.success(request, f'Producto "{nombre_producto}" eliminado exitosamente')
        return redirect('lista_productos')
    
    return render(request, 'producto/eliminar.html', {'producto': producto})