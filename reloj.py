# Importa el módulo 'time' para usar la función sleep y pausar la ejecución.
import time

# Importa 'datetime' para obtener la fecha y hora actuales.
from datetime import datetime

try:
    # Bucle infinito para mostrar la hora en tiempo real.
    while True:
        # Obtenemos la hora actual en formato HH:MM:SS.
        ahora = datetime.now().strftime("%H:%M:%S")

        # Imprimimos la hora en la misma línea, sobrescribiendo la anterior.
        print(f"\rHora actual: {ahora}", end="")

        # Pausamos la ejecución durante 1 segundo antes de actualizar la hora.
        time.sleep(1)

# Capturamos la excepción 'KeyboardInterrupt' (Ctrl + C) para detener el programa.
except KeyboardInterrupt:
    # Imprimimos un mensaje al interrumpir el reloj.
    print("\nReloj interrumpido.")
