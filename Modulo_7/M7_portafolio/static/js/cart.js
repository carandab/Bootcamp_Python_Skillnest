// Submit automatico al aumentar la cantidad en el carrito

function incrementQuantity(button, max) {
    var input = $(button).siblings('input[type="number"]');
    var currentValue = parseInt(input.val());
    
    if (currentValue < max) {
        input.val(currentValue + 1);
        $(button).closest('form').submit();
    }
}

// Submit automatico al disminuir la cantidad en el carrito
function decrementQuantity(button) {
    var input = $(button).siblings('input[type="number"]');
    var currentValue = parseInt(input.val());
    
    if (currentValue > 1) {
        input.val(currentValue - 1);
        $(button).closest('form').submit();
    }
}

$(document).ready(function() {
    
    // Submit automatico al cambiar la cantidad
    $('.quantity-form input[type="number"]').on('change', function() {
        var value = parseInt($(this).val());
        var max = parseInt($(this).attr('max'));
        var min = 1;
        
        if (value < min) {
            $(this).val(min);
        } else if (value > max) {
            $(this).val(max);
            alert('Stock máximo disponible: ' + max);
        }
        
        $(this).closest('form').submit();
    });
    
});