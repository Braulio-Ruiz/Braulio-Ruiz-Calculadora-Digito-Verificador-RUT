"""
Calculadora que permite conocer el digito verificador de un RUT.
"""
# Definición de la función, para calcular el dígito verificador
def calcular_digito_verificador(rut):
    # Lista de números para ponderar los dígitos del RUT
    multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = 0  # Inicialización de la variable suma

    # Recorremos cada dígito del RUT y hacemos el cálculo
    for i in range(8):
        digito = int(rut[7 - i])  # Tomamos un dígito de derecha a izquierda
        suma += digito * multiplicadores[i]  # Sumamos el resultado a la suma total

    resto = suma % 11  # Calculamos el resto de la suma dividido por 11

    # Comprobamos el resto para determinar el dígito verificador
    if resto == 0:
        return '0'
    elif resto == 1:
        return 'K'
    else:
        return str(11 - resto)  # Restamos el resto a 11 para obtener el dígito

# Solicitamos al usuario que ingrese el RUT
rut_ingresado = input("Por favor, escribe tu RUT sin digito verificador: ")

# Verificamos si el RUT tiene la longitud correcta y si solo contiene números
if len(rut_ingresado) == 8 and rut_ingresado.isdigit():
    # Calculamos el dígito verificador usando la función y lo almacenamos
    digito_verificador = calcular_digito_verificador(rut_ingresado)

    # Mostramos el resultado final al usuario
    print(f"Tu dígito verificador es: {digito_verificador}")
    print(f"    {rut_ingresado}-{digito_verificador}")
else:
    # Si el RUT no cumple con los requisitos, mostramos un mensaje de error
    print("Lo siento, el RUT ingresado no parece válido.")
    print(f"Rut Ingresado: {rut_ingresado}")
