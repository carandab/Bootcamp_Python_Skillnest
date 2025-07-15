$(document).ready(function() {
    // Mostrar modales
    $('#btn-1').click(function() {
        $('#modalPelicula1').modal('show');
    });
    $('#btn-2').click(function() {
        $('#modalPelicula2').modal('show');
    });
    $('#btn-3').click(function() {
        $('#modalPelicula3').modal('show');
    });
});

function confirmarReserva(modalId) {
    const modal = document.getElementById(modalId);
    
    // Obtener los valores del formulario
    const pelicula = modal.querySelector('input[type="text"][readonly]').value;
    const horario = modal.querySelector('select').value;
    const asientos = modal.querySelector('input[type="number"]').value;
    const tarjeta = modal.querySelector('input[id^="creditCard"]').value;
    const titular = modal.querySelector('input[id^="cardName"]').value;
    
    // Validar que todos los campos estén completos
    if (horario.includes("-- Selecciona") || !asientos || !tarjeta || !titular) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor completa todos los campos requeridos!',
        });
        return;
    }
    
    // Validar número de tarjeta (simulación)
    if (tarjeta.length < 16) {
        Swal.fire({
            icon: 'error',
            title: 'Tarjeta inválida',
            text: 'El número de tarjeta debe tener al menos 16 dígitos',
        });
        return;
    }
    
    // Mostrar SweetAlert con los datos
    Swal.fire({
        title: '¡Reserva Confirmada!',
        html: `
            <p><strong>Película:</strong> ${pelicula}</p>
            <p><strong>Horario:</strong> ${horario}</p>
            <p><strong>Asientos:</strong> ${asientos}</p>
            <p class="text-success mt-3">¡Disfruta de la película!</p>
        `,
        icon: 'success',
        confirmButtonText: 'OK',
        customClass: {
            popup: 'border-radius-0'
        }
    }).then(() => {
        // Cerrar el modal después de confirmar
        $('#' + modalId).modal('hide');
        
        // Resetear el formulario
        modal.querySelector('form').reset();
    });


    
}