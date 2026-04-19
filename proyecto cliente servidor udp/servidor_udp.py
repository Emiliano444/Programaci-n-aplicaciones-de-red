import socket

HOST = '127.0.0.1'
PORT = 8081

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Servidor UDP escuchando...")

data, addr = server.recvfrom(1024)
print("Cliente dice:", data.decode())

respuesta = "Hola desde UDP"
server.sendto(respuesta.encode(), addr)

server.close()
