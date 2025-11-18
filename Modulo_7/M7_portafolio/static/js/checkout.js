// Checkout JS

$(document).ready(function() {
    
    // Validación del formulario
    $('form').on('submit', function(e) {
        var shippingAddress = $('#shipping_address').val().trim();
        
        if (!shippingAddress) {
            e.preventDefault();
            alert('Por favor ingresa una dirección de envío');
            $('#shipping_address').focus();
            return false;
        }
        
        // Mostrar loading
        var submitBtn = $(this).find('button[type="submit"]');
        submitBtn.html('<i class="fas fa-spinner fa-spin me-2"></i>Procesando...');
        submitBtn.prop('disabled', true);
    });
    
    // Copiar dirección de envío a facturación
    $('#shipping_address').on('blur', function() {
        var billingAddress = $('#billing_address').val().trim();
        if (!billingAddress) {
            $('#billing_address').val($(this).val());
        }
    });
    
}); 