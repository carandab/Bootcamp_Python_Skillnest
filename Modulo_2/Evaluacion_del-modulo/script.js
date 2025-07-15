  
  /* Pop-Up de tarjetas de informacion amenazas comunes */
  
$(document).ready(function () {
  $('.card').hover(
    function () {
      $(this).css({
        'transform': 'scale(1.05)',
        'transition': 'transform 0.3s ease'
      });
    },
    function () {
      $(this).css('transform', 'scale(1)');
    }
  );
});


 /* Formulario de contacto */

 const registrosContacto = [];

  document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Evita recargar la página

    const nombre = document.getElementById('nombre').value.trim();
    const correo = document.getElementById('correo').value.trim();
    const mensaje = document.getElementById('mensaje').value.trim();

    if (nombre && correo && mensaje) {
      const nuevoRegistro = {
        nombre,
        correo,
        mensaje,
        fecha: new Date().toLocaleString()
      };

      registrosContacto.push(nuevoRegistro);

      // Mostrar en la consola
      console.log('Contacto registrado:', nuevoRegistro);

      // Guardar en localStorage
      localStorage.setItem('contactos', JSON.stringify(registrosContacto));

      alert('Mensaje enviado correctamente');

      // Limpiar formulario
      this.reset();
    } else {
      alert('Por favor, completa todos los campos.');
    }
  });


  /* Test de Seguridad */

  document.getElementById('testForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const respuestas = {
      q1: 'a',
      q2: 'a',
      q3: 'b',
      q4: 'b',
      q5: 'c'
    };

    let puntaje = 0;
    let total = Object.keys(respuestas).length;

    for (let pregunta in respuestas) {
      const seleccionada = document.querySelector(`input[name="${pregunta}"]:checked`);
      if (seleccionada && seleccionada.value === respuestas[pregunta]) {
        puntaje++;
      }
    }

    const resultado = document.getElementById('resultadoTest');
    resultado.classList.remove('d-none');
    resultado.innerText = `Tu puntaje es: ${puntaje} de ${total}.`;

    if (puntaje === total) {
      resultado.classList.remove('alert-info', 'alert-warning');
      resultado.classList.add('alert-success');
      resultado.innerText += " ¡Excelente!";
    } else if (puntaje >= 3) {
      resultado.classList.remove('alert-info', 'alert-success');
      resultado.classList.add('alert-warning');
      resultado.innerText += " ¡Buen intento!";
    } else {
      resultado.classList.remove('alert-info', 'alert-success');
      resultado.classList.add('alert-danger');
      resultado.innerText += " Necesitas repasar un poco más.";
    }
  });