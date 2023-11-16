import socket
import os
cliente =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.bind(('localhost',9999 ))
cliente.listen()

Servidor, adr= cliente.accept()
fileName= Servidor.recv(1024).decode()
print (fileName)
fileSize =Servidor.recv(1024).decode()
print (fileSize)

file = open(fileName, "wb")

fileBytes= b""
done=False
while not done:
    data=Servidor.recv(100)
    if fileBytes[-5:] == b"<End>":
        done=True
    else:
        fileBytes+=data

file.write(fileBytes)
file.close()
Servidor.close()
cliente.close()