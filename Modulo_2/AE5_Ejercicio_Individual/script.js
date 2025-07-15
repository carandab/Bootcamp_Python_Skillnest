
document.addEventListener("DOMContentLoaded", () => {

   /* Referencias a elementos del DOM */
    const solicitudesList = document.querySelector(".solicitudes-list");
    const conexionesList = document.querySelector(".connections-list");
    const contadorSolicitudes = document.getElementById("contador-solicitudes");
    const contadorConexiones = document.getElementById("contador-conexiones");

    // Actualizar contadores
    function actualizarContadores() {
        const totalSolicitudes = solicitudesList.querySelectorAll("li").length; /* selecciona todos los elementos li dentro de solicitudesList */
        const totalConexiones = conexionesList.querySelectorAll("li").length; /* selecciona todos los elementos li dentro de conexionesList */
        contadorSolicitudes.textContent = totalSolicitudes; /* crea un contador de solicitudes */
        contadorConexiones.textContent = totalConexiones; /* crea un contador de conexiones */
    }

   /* Funciones */
    
    function aceptarSolicitud(event) {
        const btn = event.target;
        const solicitudItem = btn.closest("li");
        const nombre = solicitudItem.querySelector(".solicitud-name").textContent;
        const imagenSrc = solicitudItem.querySelector("img").src;
        const alt = solicitudItem.querySelector("img").alt;

        // Crear nueva conexión
        const nuevoItem = document.createElement("li");
        nuevoItem.innerHTML = `
            <img class="connection-profile" src="${imagenSrc}" alt="${alt}">
            <span class="connection-name"><a id="connection_name" href="#">${nombre}</a></span>
        `;
        conexionesList.appendChild(nuevoItem);

        // Eliminar solicitud
        solicitudItem.remove();
        actualizarContadores();
    }

    function rechazarSolicitud(event) {
        const solicitudItem = event.target.closest("li");
        solicitudItem.remove(); 
        actualizarContadores();
    }

    // Eventos
    solicitudesList.querySelectorAll(".accept-btn").forEach(btn =>
        btn.addEventListener("click", aceptarSolicitud)
    );

    solicitudesList.querySelectorAll(".decline-btn").forEach(btn =>
        btn.addEventListener("click", rechazarSolicitud)
    );

    // Inicializar contadores
    actualizarContadores();
});

/* Editar Perfil */

document.addEventListener("DOMContentLoaded", () => {
    const editBtn = document.getElementById("edit_profile");
    let editando = false;

    editBtn.addEventListener("click", (e) => {
        e.preventDefault();

        const nombre = document.getElementById("name");
        const ubicacion = document.getElementById("location");
        const profesion = document.getElementById("occupation");
        const descripcion = document.getElementById("bio");

        if (!editando) {
            // Convertir a inputs
            nombre.innerHTML = `<input type="text" id="input-name" value="${nombre.textContent}">`;
            ubicacion.innerHTML = `<input type="text" id="input-location" value="${ubicacion.textContent}">`;
            profesion.innerHTML = `<input type="text" id="input-occupation" value="${profesion.textContent}">`;
            descripcion.innerHTML = `<textarea id="input-bio">${descripcion.textContent}</textarea>`;

            editBtn.textContent = "Guardar";
            editando = true;
        } else {
            // Guardar valores
            const nuevoNombre = document.getElementById("input-name").value;
            const nuevaUbicacion = document.getElementById("input-location").value;
            const nuevaProfesion = document.getElementById("input-occupation").value;
            const nuevaDescripcion = document.getElementById("input-bio").value;

            nombre.textContent = nuevoNombre;
            ubicacion.textContent = nuevaUbicacion;
            profesion.textContent = nuevaProfesion;
            descripcion.textContent = nuevaDescripcion;

            editBtn.textContent = "⚙︎ Editar Perfil";
            editando = false;
        }
    });
});