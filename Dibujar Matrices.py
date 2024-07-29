"""
Identificación del trabajo

Módulo: 2
Asignatura: Programacion Basica
Docente Online: Adrian Alvarez
Fecha de entrega: 07-09-2023
	
Identificación del estudiante

Nombre: Braulio Ruiz Niñoles
Carrera: Tecnico en Informatica

Ejercicio 1

Debes crear un programa que dibuje una matriz, según las siguientes consideraciones:
1. Solicitud de filas
2. Solicitud de columnas
3. Se logre dibujar filas indicadas
4. Se logre dibujar columnas solicitadas.
"""

# Solicitar el número de filas al usuario
num_filas = int(input("Ingrese el número de filas: "))

# Solicitar el número de columnas al usuario
num_columnas = int(input("Ingrese el número de columnas: "))

# Dibujar filas
for i in range(num_filas):
    # Dibuja el borde superior de la fila con "+--"
    print("+--" * num_columnas + "+")

    # Dibuja el contenido de la fila con "|  "
    print("|  " * num_columnas + "|")

# Dibujar el borde inferior de la última fila
print("+--" * num_columnas + "+")
