# CRUD de una biblioteca en memoria

# Lista para almacenar los libros
biblioteca = []

def crear_libro(id, titulo, autor):
    """Agrega un libro a la biblioteca."""
    libro = {"id": id, "titulo": titulo, "autor": autor}
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado exitosamente.")

def listar_libros():
    """Muestra todos los libros en la biblioteca."""
    if not biblioteca:
        print("La biblioteca está vacía.")
    else:
        for libro in biblioteca:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")

def actualizar_libro(id, nuevo_titulo, nuevo_autor):
    """Actualiza la información de un libro."""
    for libro in biblioteca:
        if libro["id"] == id:
            libro["titulo"] = nuevo_titulo
            libro["autor"] = nuevo_autor
            print(f"Libro con ID {id} actualizado correctamente.")
            return
    print(f"No se encontró un libro con ID {id}.")

def eliminar_libro(id):
    """Elimina un libro de la biblioteca."""
    global biblioteca
    biblioteca = [libro for libro in biblioteca if libro["id"] != id]
    print(f"Libro con ID {id} eliminado correctamente.")

# Menú para interactuar con el CRUD
def menu():
    while True:
        print("\nGestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Ver libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            id = input("ID del libro: ")
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            crear_libro(id, titulo, autor)
        elif opcion == "2":
            listar_libros()
        elif opcion == "3":
            id = input("ID del libro a actualizar: ")
            nuevo_titulo = input("Nuevo título: ")
            nuevo_autor = input("Nuevo autor: ")
            actualizar_libro(id, nuevo_titulo, nuevo_autor)
        elif opcion == "4":
            id = input("ID del libro a eliminar: ")
            eliminar_libro(id)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
