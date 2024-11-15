#Scanner de puertos de una direccion IP

import nmap

scanner = nmap.PortScanner(nmap_search_path=["C:\\Program Files (x86)\\Nmap\\nmap.exe"])

ip = input("Ingrese una dirección IP: ").strip()

print(f"\nEscaneando la IP: {ip}...\n")

try:
    scanner.scan(ip, "1-1024")
    print("Hosts encontrados:", scanner.all_hosts())

    if ip in scanner.all_hosts():
        print(f"Estado del host {ip}: {scanner[ip].state()}")
        for proto in scanner[ip].all_protocols():
            ports = scanner[ip][proto].keys()
            for port in ports:
                print(f"Puerto {port}: {scanner[ip][proto][port]['state']}")
    else:
        print("No se encontraron hosts activos con esta IP.")

except nmap.PortScannerError as e:
    print(f"Error al ejecutar Nmap: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
