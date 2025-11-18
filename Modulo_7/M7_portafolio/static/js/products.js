$(document).ready(function() {
    
    // Hacer cards clickeables
    $('.product-card').on('click', function(e) {
        // Si no se clickeó un botón o link interno
        if (!$(e.target).closest('a, button').length) {
            var url = $(this).data('href');
            if (url) {
                window.location.href = url;
            }
        }
    });
    
    // Prevenir que botones internos activen el click de la card
    $('.add-to-cart-btn, .product-actions a, .product-actions button').on('click', function(e) {
        e.stopPropagation();
    });
    
    // Animación al agregar al carrito
    $('.btn-success[href*="add_to_cart"]').on('click', function(e) {
        var button = $(this);
        var originalText = button.html();
        
        button.html('<i class="fas fa-spinner fa-spin me-2"></i>Agregando...');
        button.prop('disabled', true);
    });
    
});

// Funciones para el selector de cantidad en product detail
function incrementQuantityDetail(max) {
    var input = document.getElementById('quantity-input');
    var currentValue = parseInt(input.value);
    
    if (currentValue < max) {
        input.value = currentValue + 1;
    } else {
        alert('Stock máximo disponible: ' + max);
    }
}

function decrementQuantityDetail() {
    var input = document.getElementById('quantity-input');
    var currentValue = parseInt(input.value);
    
    if (currentValue > 1) {
        input.value = currentValue - 1;
    }
}