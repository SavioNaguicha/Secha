
class Libro:
    def _init_(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Tupla: (nombre, apellido)
        self.categoria = categoria
        self.isbn = isbn

    def _str_(self):
        return f"Título: {self.titulo}, Autor: {self.autor[0]} {self.autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def _init_(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def _str_(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def _init_(self):
        self.libros = {}  # Diccionario: isbn -> Libro
        self.usuarios = {} # Diccionario: id_usuario -> Usuario
        self.ids_usuarios = set()  # Conjunto para IDs de usuarios únicos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
        else:
            print(f"El libro con ISBN '{libro.isbn}' ya existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")
        else:
            print(f"El ID de usuario '{usuario.id_usuario}' ya está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            if libro in self.libros.values(): #Verificar si el libro está disponible
                usuario.libros_prestados.append(libro)
                del self.libros[isbn] #Eliminar el libro del diccionario de libros disponibles
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
            else:
                print(f"El libro '{libro.titulo}' no está disponible.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro #Agregar el libro de nuevo al diccionario de libros disponibles
                    print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
                    return
            print(f"El usuario '{usuario.nombre}' no tiene el libro con ISBN '{isbn}' prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro_por_isbn(self, isbn):
        if isbn in self.libros:
            return self.libros[isbn]
        else:
            return None

    def listar_libros_disponibles(self):
        if not self.libros:
            print("No hay libros disponibles en la biblioteca.")
        else:
            print("Libros disponibles:")
            for libro in self.libros.values():
                print(libro)

# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", ("Gabriel", "García Márquez"), "Ficción", "978-0307474727")
libro2 = Libro("1984", ("George", "Orwell"), "Ciencia Ficción", "978-0451524935")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Juan Pérez", 12345)
usuario2 = Usuario("María García", 67890)

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
