"""
Identifica el emisor de la tarjeta de crédito según sus primeros dígitos.
Recibe el número de la tarjeta como parámetro y retorna el nombre del emisor.
"""
def identificar_emisor(card_num):

    # Si el número de la tarjeta comienza con "4", es una tarjeta Visa.
    if card_num.startswith("4"):
        return "Visa"

    # Si comienza con alguno de los números del 51 al 55, es una MasterCard.
    elif card_num.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"

    # Si comienza con "34" o "37", es una tarjeta American Express.
    elif card_num.startswith(("34", "37")):
        return "American Express"

    # Si comienza con "6011" o "65", es una tarjeta Discover.
    elif card_num.startswith("6011") or card_num.startswith("65"):
        return "Discover"

    # Si no coincide con ningún patrón conocido, retornamos "Emisor Desconocido".
    else:
        return "Emisor Desconocido"
    
"""
Verifica si el número de tarjeta es válido usando el algoritmo de Luhn.
Retorna True si la tarjeta es válida, de lo contrario False.
"""
def luhn_check(card_num):

    # Convertimos los dígitos del número de tarjeta en una lista de enteros y la invertimos para aplicar el algoritmo de Luhn.
    digits = [int(x) for x in str(card_num)][::-1]

    # Recorremos cada segundo dígito desde la derecha y lo multiplicamos por 2.
    for i in range(1, len(digits), 2):
        digits[i] *= 2

        # Si el resultado es mayor que 9, restamos 9 para obtener un dígito único.
        if digits[i] > 9:
            digits[i] -= 9

    # Sumamos todos los dígitos y verificamos si el total es divisible por 10.
    # Retornamos True si es divisible, indicando que la tarjeta es válida.
    return sum(digits) % 10 == 0

# Solicitamos al usuario que ingrese el número de su tarjeta.
card_num = input("\nIngrese el número de su tarjeta de crédito: ").strip()

# Verificamos que el número ingresado sea válido:
# Debe ser numérico y tener entre 13 y 19 dígitos.
if not card_num.isdigit() or len(card_num) < 13 or len(card_num) > 19:
    print("\nNúmero de tarjeta inválido. Debe contener entre 13 y 19 dígitos.")

else:
    # Identificamos el emisor de la tarjeta usando la función correspondiente.
    emisor = identificar_emisor(card_num)

    # Verificamos si la tarjeta es válida usando el algoritmo de Luhn.
    if luhn_check(card_num):
        # Si es válida, mostramos el emisor y confirmamos la validez.
        print(f"\nEl número de tarjeta es válido. Emisor: {emisor}\n")
    else:
        # Si no es válida, mostramos un mensaje de error.
        print("\nEl número de tarjeta no es válido.\n")
