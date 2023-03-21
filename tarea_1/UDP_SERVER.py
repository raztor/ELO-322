from scapy.all import *
from scapy.layers.inet import IP, UDP

ORIGEN_IP = "10.35.117.52"
ORIGEN_PUERTO = 12345
DESTINO_IP = "10.35.120.69"
DESTINO_PUERTO = 54321

Mensaje = "Hola"

# Crea el paquete UDP con el payload
packet = IP(src=ORIGEN_IP, dst=DESTINO_IP)/UDP(sport=ORIGEN_PUERTO, dport=DESTINO_PUERTO)/Mensaje

send(packet)
