from socket import *
from scapy.all import *

PORT = 54321

udpSocket = socket.socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('', PORT))

# Si el paquete es valido lo decodifica de byte a string y lo imprime
while True:
    data, addr = udpSocket.recvfrom(1024)
    try:
        print(data.decode('utf-8'))
    except:
        print("Paquete invalido, reintentando...")
        continue
