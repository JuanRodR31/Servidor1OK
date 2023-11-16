import socket
import os
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect(('localhost',9999))

archivo=open("comoTanMuchacho.jpg", "rb")
tamanoArchivo= os.path.getsize("comoTanMuchacho.jpg")

servidor.send("comoTanMuchacho2.jpg".encode())
servidor.send(str(tamanoArchivo).encode())

data= archivo.read()
servidor.sendall(data)
servidor.send(b"<End>")

archivo.close()
servidor.close()