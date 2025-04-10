class Libro:
    def __init__(self, titulo, autor, Npaginas):
        self.titulo = titulo
        self.autor = autor
        self.Npaginas = Npaginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.Npaginas}")

    def actualizar_paginas(self, Npaginas):
        self.Npaginas = Npaginas
        print(f"El número de páginas ha sido actualizado a {self.Npaginas}.")

L1 = Libro("El coronel no tiene que le escriba", "Gabriel Garcias ", 2000)
L1.mostrar_informacion()

L1.actualizar_paginas(900)
L1.mostrar_informacion()