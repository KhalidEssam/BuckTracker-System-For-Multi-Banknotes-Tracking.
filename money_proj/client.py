import socket

#c= socket.socket()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect(('localhost',9000))
name = input("enter your name")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())

file = open('1.jpg', 'rb')
image_data = file.read(2048)

while image_data:
    c.send(image_data)
    image_data = file.read(2048)

file.close()
c.close()