#Building the socket.

import socket
import string
import random

server_object = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

localhost = "192.168.0.16"
port = 8000
server_object.bind((localhost, port))
server_object.listen()

#Starts the server side code.

client_socket, client_address = server_object.accept() #.accept() returns a tuple. so we unpack the tuple.]

#client_socket returns a object which is used to communicate with the client.
#client_address is the address of the client, and also the port.

if client_socket:
    #initial message showing the server has been connected.
    print("The SERVER has been successfully connected to client.")

    client_socket.send("Type a message.") #Receives the request from the client.

    request_data = client_socket.recv(1024)

    while client_socket:
        if client_socket == "stop":
            break
        else:
            print("{} : {}".format("Client Message: ", request_data.decode("utf-8")))
            server_input = random.choice(string.ascii_letters)
            client_socket.send(server_input.encode('utf-8'))
            request_data = client_socket.recv(1024)
