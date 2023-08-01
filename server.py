from ast import Str
from http import client
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print('socket created')
s.bind(('localhost',9000))
s.listen()
print('waiting')

client_socket, client_address = s.accept()
name = client_socket.recv(1024).decode()
print("client connected with " , name )
client_socket.send(bytes('welcome to our socket','utf-8'))
file = open('server_image.jpg', "wb")
image_chunk = client_socket.recv(2048)  

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)

file.close()
client_socket.close()
# while True:
#     c,adr = s.accept()
#     name = c.recv(1024).decode()
#     print("client connected with " , name )
#     file = open('recievedimage.jpg',"wb")
#     image = c.recv(2048)
#     while image:
#         file.write(image)
#         image = c.recv(2048)
#     file.close()
#     c.send(bytes('welcome to our socket','utf-8'))
#     c.close