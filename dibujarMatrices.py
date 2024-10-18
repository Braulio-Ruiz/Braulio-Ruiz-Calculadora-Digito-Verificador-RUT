"""
Permite dibujar matrices.
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
