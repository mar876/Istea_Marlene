class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

# Lista para almacenar los libros
lista_libros = []

# Libros iniciales
lista_libros.append(Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5))
lista_libros.append(Libro("1984", "George Orwell", "Ciencia Ficción", 4.3))
lista_libros.append(Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7))
lista_libros.append(Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2))
lista_libros.append(Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4))
lista_libros.append(Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1))
lista_libros.append(Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6))
lista_libros.append(Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8))
lista_libros.append(Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4))
lista_libros.append(Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0))

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    puntuacion = float(input("Ingrese la puntuación del libro (número entre 0 y 5): "))
    lista_libros.append(Libro(titulo, autor, genero, puntuacion))
    print("¡Libro agregado exitosamente!")

def buscar_libros_por_genero():
    genero = input("Ingrese el género que desea buscar: ")
    libros_en_genero = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_en_genero:
        print("Libros en el género", genero, ":")
        for titulo in libros_en_genero:
            print("-", titulo)
    else:
        print("No se encontraron libros en el género", genero)

def recomendar_libro():
    genero = input("Ingrese su género de interés: ")
    libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_en_genero:
        libro_recomendado = max(libros_en_genero, key=lambda lib: lib.puntuacion)
        print("Recomendación de libro en el género", genero, ":")
        print(libro_recomendado.titulo, "de", libro_recomendado.autor, "- Puntuación:", libro_recomendado.puntuacion)
    else:
        print("No se encontraron libros para recomendar en el género", genero)

def menu():
    while True:
        print("\n--- Sistema de Recomendación de Libros ---")
        print("1. Agregar Libro")
        print("2. Buscar Libros por Género")
        print("3. Recomendar Libro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libros_por_genero()
        elif opcion == "3":
            recomendar_libro()
        elif opcion == "4":
            print("¡Gracias por usar el sistema de recomendación de libros!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar la aplicación
menu()
