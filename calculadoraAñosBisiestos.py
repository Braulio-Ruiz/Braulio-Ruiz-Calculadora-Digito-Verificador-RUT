"""
Calculadora de Años Bisiestos, dependiendo del año de nacimiento.
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
