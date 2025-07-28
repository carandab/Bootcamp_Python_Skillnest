// Capturar envío del formulario
const form = document.querySelector('#contacto form');
form.addEventListener('submit', (event) => {
  event.preventDefault();

  const nombre = form.querySelector('input[type="text"]').value.trim();
  const email = form.querySelector('input[type="email"]').value.trim();
  const mensaje = form.querySelector('textarea').value.trim();

  console.log('Formulario enviado:');
  console.log('Nombre:', nombre);
  console.log('Email:', email);
  console.log('Mensaje:', mensaje);

  Swal.fire({
    icon: 'success',
    title: 'Mensaje enviado',
    html: `<p>Gracias, <strong>${nombre}</strong>, por contactarnos.<br>
           Te responderemos pronto a <strong>${email}</strong>.</p>`,
    confirmButtonText: 'Aceptar'
  });

  form.reset();
});


/* Skill Bars */

$(document).ready(function() {
    
    // Inicializar barras de progreso en 0%
    $('.skill-progress-bar').css('width', '0%');
    
    // Mostrar todos los elementos small desde el inicio
    $('.ht small').css({
        'opacity': '1',
        'transform': 'translateY(0)'
    });
    
    // Asignar clases de color según el porcentaje
    $('.ht').each(function() {
        const $progressBar = $(this).find('.skill-progress-bar');
        const targetWidth = parseInt($progressBar.data('width').replace('%', ''));
        
        // Limpiar clases previas y asignar según el nivel
        $progressBar.removeClass('advanced intermediate basic beginner');
        
        if (targetWidth >= 80) {
            $progressBar.addClass('advanced');
        } else if (targetWidth > 60) {
            $progressBar.addClass('intermediate');
        } else if (targetWidth >= 40) {
            $progressBar.addClass('basic');
        } else {
            $progressBar.addClass('beginner');
        }
    });
    
    // Función para animar una barra específica
    function animateSkillBar($element) {
        const $progressBar = $element.find('.skill-progress-bar');
        const targetWidth = $progressBar.data('width');
        
        // Animar la barra de progreso
        $progressBar.css({
            'width': targetWidth,
            'transition': 'width 1.5s ease-out'
        });
        
        // Marcar como animado para evitar repetir la animación
        $element.addClass('animated');
    }
    
    // Intersection Observer para detectar cuando las barras son visibles
    const observerOptions = {
        threshold: 0.3, // Se activa cuando el 30% del elemento es visible
        rootMargin: '0px 0px -50px 0px' // Se activa un poco antes de que sea completamente visible
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                const $element = $(entry.target);
                
                // Solo animar si no ha sido animado antes
                if (!$element.hasClass('animated')) {
                    // Pequeño delay para efecto escalonado
                    const delay = $element.index() * 200; // 200ms entre cada barra
                    
                    setTimeout(function() {
                        animateSkillBar($element);
                    }, delay);
                }
            }
        });
    }, observerOptions);
    
    // Observar todos los elementos de habilidades técnicas
    $('.ht').each(function() {
        observer.observe(this);
    });
});

