import socket

HOST = '127.0.0.1'
PORT = 8080
"""
socket.connect 
La conexión se vuelve remota 
"""
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

mensaje = "Necesito la conexión"
cliente.sendall(mensaje.encode())

data = cliente.recv(1024)
print('servidor responde', data.decode())

cliente.close()
