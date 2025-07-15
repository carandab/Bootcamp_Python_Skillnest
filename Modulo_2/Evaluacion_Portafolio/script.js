// Mostrar barra de progreso al hacer hover
$('#habilidades-Tecnicas').hover(
  function() {
    $(this).addClass('mostrar-barras');
  },
  function() {
    $(this).removeClass('mostrar-barras');
  }
);

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