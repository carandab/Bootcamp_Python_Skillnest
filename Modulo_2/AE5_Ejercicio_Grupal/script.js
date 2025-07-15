// Datos de libros (catálogo)
   const libros = [
    {
        id: 1,
        titulo: "Cien años de soledad",
        autor: "Gabriel García Márquez",
        genero: "Realismo mágico",
        sinopsis: "La saga de la familia Buendía en el pueblo mítico de Macondo. Una obra maestra de la literatura latinoamericana que narra la historia de varias generaciones de una familia y su relación con un pueblo imaginario."
    },
    {
        id: 2,
        titulo: "1984",
        autor: "George Orwell",
        genero: "Ciencia ficción",
        sinopsis: "Una distopía clásica sobre un estado totalitario donde el gobierno controla cada aspecto de la vida. Winston Smith lucha por mantener su humanidad en un mundo de vigilancia constante y manipulación de la verdad."
    },
    {
        id: 3,
        titulo: "Orgullo y prejuicio",
        autor: "Jane Austen",
        genero: "Romance",
        sinopsis: "La historia de Elizabeth Bennet y su relación con el señor Darcy en la Inglaterra del siglo XIX. Una comedia de costumbres que explora temas de educación, matrimonio y posición social."
    },
    {
        id: 4,
        titulo: "El señor de los anillos",
        autor: "J.R.R. Tolkien",
        genero: "Fantasía",
        sinopsis: "La épica lucha por destruir el Anillo Único y salvar la Tierra Media. Una obra monumental que sigue el viaje de Frodo Bolsón y la Comunidad del Anillo a través de tierras peligrosas."
    },
    {
        id: 5,
        titulo: "Harry Potter y la piedra filosofal",
        autor: "J.K. Rowling",
        genero: "Fantasía",
        sinopsis: "El inicio de la saga del joven mago Harry Potter, quien descubre en su undécimo cumpleaños que es el hijo de dos poderosos magos y posee poderes mágicos. Comienza su educación en el Colegio Hogwarts de Magia y Hechicería."
    },
    {
        id: 6,
        titulo: "Crónica del pájaro que da cuerda al mundo",
        autor: "Haruki Murakami",
        genero: "Realismo mágico",
        sinopsis: "Una novela compleja y surrealista que sigue a Toru Okada mientras busca a su gato desaparecido y se ve envuelto en una serie de eventos extraños y personajes peculiares que cambiarán su vida para siempre."
    },
    {
        id: 7,
        titulo: "Dune",
        autor: "Frank Herbert",
        genero: "Ciencia ficción",
        sinopsis: "Ambientada en el desértico planeta Arrakis, narra la historia de Paul Atreides y su ascenso como líder mesiánico mientras lucha por controlar la especia más valiosa del universo."
    },
    {
        id: 8,
        titulo: "Crimen y castigo",
        autor: "Fiódor Dostoyevski",
        genero: "Ficción psicológica",
        sinopsis: "La historia del estudiante Raskólnikov, quien planea y ejecuta un asesinato y luego debe lidiar con las consecuencias psicológicas y morales de sus acciones."
    }
];

// Referencias a elementos del DOM
const searchInput = document.getElementById('search-input');
const searchBtn = document.getElementById('search-btn');
const bookList = document.getElementById('book-list');
const registerForm = document.getElementById('register-form');
const resultCount = document.getElementById('result-count');

// Mostrar libros al cargar la página
function mostrarLibros(librosAMostrar) {
    bookList.innerHTML = '';
    
    if (librosAMostrar.length === 0) {
        bookList.innerHTML = `
            <div class="no-results">
                <p>No se encontraron libros que coincidan con tu búsqueda</p>
                <p>Intenta con otro término o revisa nuestro catálogo completo</p>
            </div>
        `;
        resultCount.textContent = "0 libros encontrados";
        return;
    }
    
    
    librosAMostrar.forEach(libro => {
        const libroElement = document.createElement('div');
        libroElement.className = 'book-card';
        libroElement.innerHTML = `
            
            <div class="card">
                <h3>${libro.titulo}</h3>
                <div class="book-meta">
                    <span><strong>Autor:</strong> ${libro.autor}</span>
                    <span><strong>Género:</strong> ${libro.genero}</span>
                </div>
                <p class="book-description" id="contador">${libro.sinopsis}</p>
            </div>
        `;
        bookList.appendChild(libroElement);
    });
    
// Actualizar contador de resultados
    resultCount.textContent = `${librosAMostrar.length} libros encontrados`;
}

// Buscar libros en todos los campos
function buscarLibros() {
    const termino = searchInput.value.toLowerCase().trim();
    
    if (termino === '') {
        mostrarLibros(libros);
        return;
    }
    
    const resultados = libros.filter(libro => 
        libro.titulo.toLowerCase().includes(termino) ||
        libro.autor.toLowerCase().includes(termino) ||
        libro.genero.toLowerCase().includes(termino)
    );
    
    mostrarLibros(resultados);
}

// Funcion de valizacion de registro 

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validarRegistro(event) {
    event.preventDefault();

    const nombre = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (!nombre || !email || !password || !confirmPassword) {
        alert('Todos los campos son obligatorios');
        return;
    }

    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden');
        return;
    }

    if (password.length < 6) {
        alert('La contraseña debe tener al menos 6 caracteres');
        return;
    }

    if (!validateEmail(email)) {
        alert('Por favor ingresa un email válido');
        return;
    }

    const datosUsuario = {
        nombre,
        email,
        password
    };

    console.log("📝 Datos registrados:", datosUsuario);
    alert('¡Registro exitoso!');
    registerForm.reset();
}


registerForm.addEventListener('submit', validarRegistro);


// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    mostrarLibros(libros);
});

searchBtn.addEventListener('click', buscarLibros);

searchInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); 
        buscarLibros();
    }
});

/* searchInput.addEventListener('input', buscarLibros); // Búsqueda en tiempo real */
