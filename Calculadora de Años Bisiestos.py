"""
Identificación del trabajo

Módulo: 2
Asignatura: Programacion Basica
Docente Online: Adrian Alvarez
Fecha de entrega: 07-09-2023
	
Identificación del estudiante

Nombre: Braulio Ruiz Niñoles
Carrera: Tecnico en Informatica
"""

"""
Ejercicio 3

Un año bisiesto es un año con 366 días en vez de 365. Cada 4 años, febrero tiene un día más. Esto se 
hace porque un año oficialmente no tiene 365 días, sino 365,25 días. Añadiendo un día cada 4 años, se 
soluciona este problema.
Cualquier año divisible por 4 es un año bisiesto, como 2016, 2020, 2024, 2028.
Nota: La regla anterior no se aplica a los años de siglo.
Siglos como 1900 y 2000 solo tienen un día bisiesto si son divisibles por 400.
1900 es divisible entre 4 y también entre 100, pero no entre 400, por lo que no es un año bisiesto.
Esto significa que los siglos son solo un año bisiesto si son divisibles por 400.
Entonces 1900 no lo es, 2000 lo es, 2100, 2200, 2300 no lo es, pero 2400 es otro año bisiesto.

Cree un programa, donde:
1. Dado el año de nacimiento de una persona
2. El año de muerte
3. Ingresar un cero en caso de estar vivo aún
4. El sistema debe reemplazar el cero por el año actual
5. se determine la cantidad de años bisiestos que le ha tocado vivir.
"""
# Solicitamos el año de nacimiento como entrada del usuario
año_nacimiento = int(input("Ingrese el año de nacimiento: "))

# Solicitamos el año de muerte (o 0 si está vivo) como entrada del usuario
año_muerte = int(input("Ingrese el año de muerte (o 0 si está vivo): "))

# Si el año de muerte es 0, lo reemplazamos con el año actual
if año_muerte == 0:
    import datetime
    año_muerte = datetime.date.today().year

# Función para determinar si un año es bisiesto
def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4, pero no por 100 (excepto si es divisible por 400)
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# Contador para llevar un registro de los años bisiestos
cantidad_bisiestos = 0

# Iteramos a través de los años desde el año de nacimiento hasta el año de muerte
for año in range(año_nacimiento, año_muerte + 1):
    if es_bisiesto(año):
        cantidad_bisiestos += 1

# Imprimimos la cantidad de años bisiestos vividos
print(f"La cantidad de años bisiestos vividos es: {cantidad_bisiestos}")

