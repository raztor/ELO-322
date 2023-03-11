from scapy.all import *
from scapy.layers.inet import IP, UDP

ORIGEN_IP = "192.168.100.20"
ORIGEN_PUERTO = 12345
DESTINO_IP = "192.168.100.139"
DESTINO_PUERTO = 54321

Mensaje = "Hola"

# Crea el paquete UDP con el payload
packet = IP(src=ORIGEN_IP, dst=DESTINO_IP)/UDP(sport=ORIGEN_PUERTO, dport=DESTINO_PUERTO)/Mensaje

send(packet)
