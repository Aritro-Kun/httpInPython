#We will be creating a HTTP Server using Python.
#The server can handle basic requests such as GET, POST, DELETE & PUT

import socket 

#This is the module that is required to be imported.

server_object = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

#AF_INET is the address family for IPv4
#SOCK_STREAM is the socket type TCP connections, since HTTP is built over TCP it has the same type.

ip_address = "192.168.0.16"
port = 8000
server_object.bind((ip_address, port)) #The socket object gets bounded to the initialised IP Address and the Port.
server_object.listen() #Once, binding is done, now the server object is to listen to the object.
