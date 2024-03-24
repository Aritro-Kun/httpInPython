import socket

server_socket = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)

localhost = "192.168.0.16"
port = 8000
server_socket.bind((localhost, port))
server_socket.listen()

print("Establishing Connection to the server. \n")

client_socket, client_address = server_socket.accept()

if client_socket:
    print("Connection to the server is established, successfully.")

    client_socket.send("Specify the method of request [GET, POST, DELETE, PUT] or [STOP]: ".encode(encoding="utf-8", errors = "strict"))
    #sockets deal with bytes and not strings, so, .send() can only access unicode characters, for this reason we encode it to utf-8 so that the .send of sockets can access it and do the necessary task.

    #Since, the method cannot be wrong and needs to specific, we are using the error as strict.

    while True:
        client_request_data = client_socket.recv(1024).decode('utf-8').strip()
        #the .decode() function works exactly opposite to that of the .encode(), the .decode() takes in the utf-8, in which the string is already encoded in. It converts it to the original string.
        #strips the extra blanks, that maybe provided as input.
        if client_request_data.upper() == "STOP":
            break
        elif client_request_data.upper() in ["GET", "POST", "DELETE", "PUT"]:
            response_to_client = "You have chosen the client_request_data.upper() method."
        else:
            response_to_client = "You have not chosen an appropriate method."
        client_socket.send(response_to_client.encode("utf-8"))
    
print("Server disconnected successfully.")
client_socket.close()
server_socket.close()