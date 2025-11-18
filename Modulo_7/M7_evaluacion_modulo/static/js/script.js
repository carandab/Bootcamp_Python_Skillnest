// Gestor de Productos - JavaScript Principal

document.addEventListener('DOMContentLoaded', function() {
    
/*     // Auto-cerrar alertas después de 5 segundos
    // NO auto-cerrar en páginas de eliminación
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    const isDeletePage = window.location.pathname.includes('/eliminar/');
    
    if (!isDeletePage) {
        alerts.forEach(alert => {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 15000);
        });
    }
 */

    
    // Confirmación antes de eliminar
    const deleteButtons = document.querySelectorAll('.btn-delete, [data-confirm]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const message = this.dataset.confirm || '¿Estás seguro de que deseas eliminar este elemento?';
            if (!confirm(message)) {
                e.preventDefault();
                return false;
            }
        });
    });

    // Animación de aparición para cards
    const cards = document.querySelectorAll('.card, .stat-card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                cardObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        cardObserver.observe(card);
    });

    // Validación de formularios
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Búsqueda en tiempo real (si existe input de búsqueda)
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                // Puedes agregar lógica AJAX aquí
                console.log('Buscando:', this.value);
            }, 300);
        });
    }

    // Tooltips de Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Preview de imagen (si hay input file para imágenes)
    const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    imageInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const preview = document.getElementById('imagePreview');
                    if (preview) {
                        preview.src = e.target.result;
                        preview.classList.remove('d-none');
                    }
                };
                reader.readAsDataURL(file);
            }
        });
    });

    // Contador de caracteres para textareas
    const textareas = document.querySelectorAll('textarea[maxlength]');
    textareas.forEach(textarea => {
        const maxLength = textarea.getAttribute('maxlength');
        const counter = document.createElement('small');
        counter.className = 'form-text text-muted';
        textarea.parentNode.appendChild(counter);

        const updateCounter = () => {
            const remaining = maxLength - textarea.value.length;
            counter.textContent = `${remaining} caracteres restantes`;
            if (remaining < 50) {
                counter.classList.add('text-warning');
            } else {
                counter.classList.remove('text-warning');
            }
        };

        textarea.addEventListener('input', updateCounter);
        updateCounter();
    });

    // Formatear números de precio mientras se escribe
    const priceInputs = document.querySelectorAll('input[name*="precio"]');
    priceInputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value) {
                const value = parseFloat(this.value);
                if (!isNaN(value)) {
                    this.value = value.toFixed(2);
                }
            }
        });
    });

    // Confirmación mejorada para formularios de eliminación
    const deleteForm = document.querySelector('.delete-form');
    if (deleteForm) {
        deleteForm.addEventListener('submit', function(e) {
            const itemName = this.dataset.itemName || 'este elemento';
            if (!confirm(`¿Estás completamente seguro de eliminar "${itemName}"? Esta acción no se puede deshacer.`)) {
                e.preventDefault();
                return false;
            }
        });
    }

    // Toggle para mostrar/ocultar filtros avanzados
    const toggleFilters = document.getElementById('toggleFilters');
    if (toggleFilters) {
        toggleFilters.addEventListener('click', function() {
            const advancedFilters = document.getElementById('advancedFilters');
            advancedFilters.classList.toggle('d-none');
            const icon = this.querySelector('i');
            icon.classList.toggle('bi-chevron-down');
            icon.classList.toggle('bi-chevron-up');
        });
    }

    // Ordenamiento de tablas (básico)
    const sortableHeaders = document.querySelectorAll('th[data-sort]');
    sortableHeaders.forEach(header => {
        header.style.cursor = 'pointer';
        header.addEventListener('click', function() {
            const column = this.dataset.sort;
            console.log('Ordenar por:', column);
            // Aquí puedes implementar la lógica de ordenamiento
        });
    });

    // Navegación suave para anclas
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Loading state para botones de submit
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(button => {
        button.closest('form')?.addEventListener('submit', function() {
            if (this.checkValidity()) {
                button.disabled = true;
                const originalText = button.innerHTML;
                button.innerHTML = '<span class="spinner"></span> Procesando...';
                
                // Re-habilitar después de 5 segundos (por si hay error)
                setTimeout(() => {
                    button.disabled = false;
                    button.innerHTML = originalText;
                }, 5000);
            }
        });
    });

    // Resaltar campo activo en formularios
    const formInputs = document.querySelectorAll('.form-control, .form-select');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.closest('.mb-3')?.classList.add('focused');
        });
        input.addEventListener('blur', function() {
            this.closest('.mb-3')?.classList.remove('focused');
        });
    });

    // Manejo de etiquetas múltiples
    const checkboxGroups = document.querySelectorAll('.checkbox-group');
    checkboxGroups.forEach(group => {
        const checkboxes = group.querySelectorAll('input[type="checkbox"]');
        const counter = document.createElement('small');
        counter.className = 'form-text text-muted';
        group.appendChild(counter);

        const updateCounter = () => {
            const checked = Array.from(checkboxes).filter(cb => cb.checked).length;
            counter.textContent = checked > 0 ? `${checked} seleccionado(s)` : 'Ninguno seleccionado';
        };

        checkboxes.forEach(cb => {
            cb.addEventListener('change', updateCounter);
        });
        updateCounter();
    });

    console.log('✅ Gestor de Productos JavaScript cargado correctamente');
});