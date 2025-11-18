// Forms JS

$(document).ready(function() {
    
    // Auto-focus en primer campo
    $('input:not([type="hidden"]):first').focus();
    
    // Toggle password visibility (opcional)
    $('.toggle-password').on('click', function() {
        var input = $(this).siblings('input');
        var icon = $(this).find('i');
        
        if (input.attr('type') === 'password') {
            input.attr('type', 'text');
            icon.removeClass('fa-eye').addClass('fa-eye-slash');
        } else {
            input.attr('type', 'password');
            icon.removeClass('fa-eye-slash').addClass('fa-eye');
        }
    });
    
    // Validación de contraseñas iguales en registro
    $('#id_password2').on('blur', function() {
        var pass1 = $('#id_password1').val();
        var pass2 = $(this).val();
        
        if (pass1 && pass2 && pass1 !== pass2) {
            $(this).addClass('is-invalid');
        } else {
            $(this).removeClass('is-invalid');
        }
    });
    
    // Loading state en submit
    $('form').on('submit', function() {
        var submitBtn = $(this).find('button[type="submit"]');
        var originalText = submitBtn.html();
        
        submitBtn.html('<i class="fas fa-spinner fa-spin me-2"></i>Procesando...');
        submitBtn.prop('disabled', true);
    });
    
});