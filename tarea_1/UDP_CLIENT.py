from socket import *
from scapy.all import *

def create_socket():
    PORT = 54321
    udpSocket = socket.socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', PORT))

with create_socket() as udpSocket:
    while True:
        data, addr = udpSocket.recvfrom(1024)
        try:
            print(data.decode('utf-8'))
        except:
            print("Paquete invalido, reintentando...")
            continue
