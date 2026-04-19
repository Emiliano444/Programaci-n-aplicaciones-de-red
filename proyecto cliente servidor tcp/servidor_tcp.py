'''
---Para crear sockets---
Necesitamos
Dirección IP(protocolo de internet)
AF_INET, AF_INET6,  AD_UNIX, AF_CAN, AF_PACKET, AF RDS


Protocolo de conexión (servicios)
SOCK_DGRAM, SOCK_RAW,CAN_BCM, CAN_ISOTP, CAN_j1939 

Estructura 
class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

'''
import socket

#PORT 8080 TCP/UDP alternavita al #PORT 80 HTTP
HOST = '127.0.0.1' #IPv4
PORT = 8080 #int


#familia de direcciones y conexiones por defecto
server = socket.socket(
      socket.AF_INET, 
      socket.SOCK_STREAM)

"""
socket.bind or class.bind(address)
Asigna una dirección a nuestra clase socket
Estado de escucha

socket.accept(conn, addres)
conn: el socket creado ahora puede recibir y envia datos en la conexón

conn.recv()
Recibir datos desde la red
1024 = Tamaño máximo de datos que vas a recibir (bytes)

data.decode()
Decodifica a texto los bytes

dat.decode()
Codifica texto a formato byte, desde el otro extremo el cliente decodfica los datos en texto
"""

server.bind((HOST, PORT))
server.listen()

print('servidor TCP escuchando...')


conn, addr = server.accept()
print(f'conectando por {addr}')

data = conn.recv(1024)
print('cliente dice:', data.decode())

respuesta = 'hola cliente, mensaje recibido'
conn.sendall(respuesta.encode())

conn.close()
server.close() 
