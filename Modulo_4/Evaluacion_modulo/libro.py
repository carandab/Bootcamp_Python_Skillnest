class Libro:
    
    def __init__(self, titulo, autor, fecha_publicacion, estado="disponible"):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.fecha_publicacion}, Estado: {self.estado}"

    # Getters

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_fecha_publicacion(self):
        return self.fecha_publicacion
    
    def get_estado(self):
        return self.estado

    # Setters

    def set_titulo(self, nuevo_titulo):

        if nuevo_titulo and nuevo_titulo.strip():
            self.titulo = nuevo_titulo.strip()
        else:
            raise ValueError("El título no puede estar vacío")
    
    def set_autor(self, nuevo_autor):

        if nuevo_autor and nuevo_autor.strip():
            self.autor = nuevo_autor.strip()
        else:
            raise ValueError("El autor no puede estar vacío")
    
    def set_fecha_publicacion(self, nueva_fecha):

        if isinstance(nueva_fecha, int) and nueva_fecha > 0:
            self.fecha_publicacion = nueva_fecha
        else:
            raise ValueError("La fecha de publicación debe ser un año válido (número entero positivo)")
    
    def set_estado(self, nuevo_estado):

        estados_validos = ["disponible", "prestado"]

        if nuevo_estado.lower() in estados_validos:
            self.estado = nuevo_estado.lower()
        else:
            raise ValueError(f"Estado inválido. Debe ser: {' o '.join(estados_validos)}")
            
    # Métodos para cambiar estado

    def prestar(self):

        if self.estado == "disponible":
            self.estado = "prestado"
        else:
            raise Exception("El libro ya está prestado.")

    def devolver(self):

        if self.estado == "prestado":
            self.estado = "disponible"
        else:
            raise Exception("El libro no está prestado.")
            
    def esta_disponible(self):
        return self.estado == "disponible"

class LibroDigital(Libro):
    
    def __init__(self, titulo, autor, fecha_publicacion, formato, estado="disponible"):
        super().__init__(titulo, autor, fecha_publicacion, estado)
        self.formato = formato
    
    def get_formato(self):
        return self.formato
    
    def set_formato(self, nuevo_formato):

        formatos_validos = ["PDF", "EPUB", "MOBI"]

        if nuevo_formato.upper() in formatos_validos:
            self.formato = nuevo_formato.upper()
        else:
            raise ValueError(f"Formato inválido. Debe ser: {', '.join(formatos_validos)}")
    
    # Polimorfismo de __str__
    
    def __str__(self):
        return f"Digital, {super().__str__()}, Formato: {self.formato}"


# Pruebas

if __name__ == "__main__":

    # Prueba de la clase Libro

    libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
    print("Libro creado:", libro1)
    
    # Prueba de getters y setters

    print(f"Título: {libro1.get_titulo()}")
    print(f"Estado actual: {libro1.get_estado()}")
    
    # Cambiar estado usando setter

    libro1.set_estado("prestado")
    print(f"Estado después de cambiar: {libro1.get_estado()}")
    print("Libro actualizado:", libro1)
    
    print("\n" + "-"*50)
    
    # Prueba de LibroDigital
    
    libro_digital = LibroDigital("1984", "George Orwell", 1949, "PDF")
    print("Libro digital creado:", libro_digital)
    
    # Probar setter de formato
    libro_digital.set_formato("EPUB")
    print("Después de cambiar formato:", libro_digital)