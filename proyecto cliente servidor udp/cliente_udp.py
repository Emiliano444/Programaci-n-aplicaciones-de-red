import socket

HOST = '127.0.0.1'
PORT = 8081

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensaje = "Hola servidor UDP"
client.sendto(mensaje.encode(), (HOST, PORT))

data, addr = client.recvfrom(1024)
print("Servidor responde:", data.decode())

client.close()
