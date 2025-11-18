from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction, IntegrityError
from products.models import Product
from .models import Order, OrderItem


@login_required
def checkout(request):

    # Obtener carrito de la sesión
    cart = request.session.get('cart', {})
    
    # Validar que el carrito no esté vacío
    if not cart:
        messages.error(request, 'Tu carrito está vacío.')
        return redirect('products:cart_view')
    
    # Obtener productos del carrito
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        total += subtotal
    
    # Si el usuario ha enviado el formulario, crear el pedido
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address', '').strip()
        billing_address = request.POST.get('billing_address', '').strip()
        notes = request.POST.get('notes', '').strip()
        
        # Validaciones
        if not shipping_address:
            messages.error(request, 'La dirección de envío es obligatoria.')
            return render(request, 'orders/checkout.html', {
                'cart_items': cart_items,
                'total': total
            })
        
        try:
            with transaction.atomic():
                # 1. Crear el Order
                order = Order.objects.create(
                    customer=request.user,
                    shipping_address=shipping_address,
                    billing_address=billing_address,
                    notes=notes,
                    status='Pending'
                )
                
                # 2. Crear OrderItems desde el carrito
                for item in cart_items:
                    # Verificar stock disponible
                    if item['product'].stock < item['quantity']:
                        raise ValueError(
                            f"Stock insuficiente para {item['product'].name}. "
                            f"Disponible: {item['product'].stock}, Solicitado: {item['quantity']}"
                        )
                    
                    # Crear OrderItem
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        quantity=item['quantity'],
                        unit_price=item['product'].price
                    )
                    
                    # Reducir stock (opcional - comentar si no quieres esto ahora)
                    item['product'].stock -= item['quantity']
                    item['product'].save()
                
                # 3. Calcular y guardar el total
                order.calculate_total()
                
                # 4. Limpiar el carrito de la sesión
                request.session['cart'] = {}
                request.session.modified = True
                
                # 5. Mensaje de éxito
                messages.success(
                    request,
                    f'¡Pedido #{order.id} creado exitosamente! Total: ${order.total}'
                )
                
                # 6. Redirigir a detalle del pedido
                return redirect('orders:detalle_pedido', pk=order.id)
        
        # Manejo de errores
        except IntegrityError:
            messages.error(request, 'Error al crear el pedido. Inténtalo de nuevo.')
            return render(request, 'orders/checkout.html', {
                'cart_items': cart_items,
                'total': total
            })
        
        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'orders/checkout.html', {
                'cart_items': cart_items,
                'total': total
            })
        
        except Exception as e:
            messages.error(request, f'Error al procesar el pedido: {str(e)}')
            return render(request, 'orders/checkout.html', {
                'cart_items': cart_items,
                'total': total
            })
    
    # GET - Mostrar formulario de checkout
    # Pre-llenar con datos del perfil si existen
    user_profile = None
    if hasattr(request.user, 'cliente_profile'):
        user_profile = request.user.cliente_profile
    
    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'user_profile': user_profile
    })


# Detalle de un pedido específico

@login_required
def order_detail(request, pk):

    order = get_object_or_404(Order, pk=pk, customer=request.user)
    order_items = order.items.select_related('product').all()
    
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'order_items': order_items
    })

# Lista de pedidos del usuario

@login_required
def order_list(request):

    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    
    return render(request, 'orders/order_list.html', {
        'orders': orders
    })