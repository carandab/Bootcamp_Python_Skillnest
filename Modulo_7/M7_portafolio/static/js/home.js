$(document).ready(function() {
    
    // Hacer cards clickeables
    $('.product-card').on('click', function(e) {
        if (!$(e.target).closest('a, button').length) {
            var url = $(this).data('href');
            if (url) {
                window.location.href = url;
            }
        }
    });
    
    // Prevenir que botones activen el click de la card
    $('.add-to-cart-btn').on('click', function(e) {
        e.stopPropagation();
    });
    
    // Scroll suave
    $('.btn[href^="#"]').on('click', function(e) {
        e.preventDefault();
        var target = $(this.getAttribute('href'));
        if(target.length) {
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 80
            }, 1000);
        }
    });
    
    // Lazy loading de imágenes
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
});