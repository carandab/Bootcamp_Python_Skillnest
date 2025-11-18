$(document).ready(function() {
    
    // Esconder mensajes de alerta después de 5 segundos
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);
    
    // Smooth scrolling para enlaces de ancla
    $('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        
        var target = this.hash;
        var $target = $(target);
        
        if ($target.length) {
            $('html, body').animate({
                'scrollTop': $target.offset().top - 80
            }, 500);
        }
    });
    
    // Resaltar el enlace activo en la barra de navegación
    var url = window.location.href;
    $('.navbar-nav .nav-link').each(function() {
        if (this.href === url) {
            $(this).addClass('active');
        }
    });
});