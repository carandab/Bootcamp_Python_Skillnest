import os
from libro import Libro, LibroDigital

class Biblioteca:

    def __init__(self):
        self.libros = []
        self.cargar_libros()

# Métodos

    def agregar_libro(self, libro):

        if isinstance(libro, (Libro, LibroDigital)):

            if not self.buscar_libro(libro.get_titulo()):

                self.libros.append(libro)
                print(f"Libro '{libro.get_titulo()}' agregado exitosamente.")
                return True
            
            else:
                raise Exception(f"Ya existe un libro con el título '{libro.get_titulo()}'")
            
        else:
            raise ValueError("El objeto debe ser una instancia de Libro o LibroDigital")

    def eliminar_libro(self, titulo):

        libro_encontrado = self.buscar_libro(titulo)

        if libro_encontrado:

            self.libros.remove(libro_encontrado)
            print(f"Libro '{titulo}' eliminado exitosamente.")
            return True
        
        else:
            raise Exception(f"No se encontró el libro '{titulo}' en la biblioteca")    
        
    def mostrar_lista(self):

        if not self.libros:
            
            print("La biblioteca está vacía.")
            return
        
        print("\n=== Inventario de Libros ===")

        for i, libro in enumerate(self.libros, 1):
            print(f"{i}. {libro}")

    def mostrar_disponibles(self):

        libros_disponibles = [libro for libro in self.libros if libro.esta_disponible()]
        
        if not libros_disponibles:
            print("No hay libros disponibles actualmente.")
            return
        
        print("\n=== LIBROS DISPONIBLES ===")
        for i, libro in enumerate(libros_disponibles, 1):
            print(f"{i}. {libro}")

    def buscar_libro(self, titulo):

        titulo_busqueda = titulo.lower().strip()
        
        libros_encontrados = []
        
        for libro in self.libros:

            if titulo_busqueda in libro.get_titulo().lower():
                libros_encontrados.append(libro)
        
        return libros_encontrados
    
    def prestar_libro(self, titulo):

        libro = self.buscar_libro(titulo)

        if libro:
            try:
                libro.prestar()
                print(f"El libro '{titulo}' ha sido prestado exitosamente.")
                return True
            except Exception as e:
                raise e
        else:
            raise Exception(f"No se encontró el libro '{titulo}' en la biblioteca")
        
    def devolver_libro(self, titulo):

        libro = self.buscar_libro(titulo)

        if libro:
            try:
                libro.devolver()
                print(f"El libro '{titulo}' ha sido devuelto exitosamente.")
                return True
            except Exception as e:
                raise e
        else:
            raise Exception(f"No se encontró el libro '{titulo}' en la biblioteca")

    # Manejo de Archivos

    def cargar_libros(self):
        
        try:
            with open("inventario.txt", "r", encoding="utf-8") as archivo:

                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        try:
                            partes = linea.split(" - ")
                            if len(partes) >= 5:
                                titulo = partes[0].strip()
                                autor = partes[1].strip()
                                año = int(partes[2].strip())
                                estado = partes[3].strip()
                                tipo = partes[4].strip().lower()
                                
                                if tipo.lower() == "digital" and len(partes) >= 6:
                                    formato = partes[5].strip()
                                    libro = LibroDigital(titulo, autor, año, formato, estado)
                                else:
                                    libro = Libro(titulo, autor, año, estado)
                                
                                self.libros.append(libro)
                        except (ValueError, IndexError) as e:
                            print(f"Error al procesar línea: {linea}. Error: {e}")

            print("Libros cargados desde inventario.txt")

        except FileNotFoundError:
            print("El archivo 'inventario.txt' no se encontró. Se creará uno nuevo al guardar.")

        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def guardar_archivo(self):

        try:

            with open("inventario.txt", "w", encoding="utf-8") as archivo:
                for libro in self.libros:
                    estado_cap = libro.get_estado().capitalize()
                    
                    if isinstance(libro, LibroDigital):
                        linea = f"{libro.get_titulo()} - {libro.get_autor()} - {libro.get_fecha_publicacion()} - {estado_cap} - Digital - {libro.get_formato()}\n"
                    else:
                        linea = f"{libro.get_titulo()} - {libro.get_autor()} - {libro.get_fecha_publicacion()} - {estado_cap} - Físico\n"
                    archivo.write(linea)

            print("Biblioteca guardada con éxito")

        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

