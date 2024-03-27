import socket

client_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

server_address = "192.168.0.16"
server_port = 3000
client_socket.connect((server_address, server_port))

print("Connection to the server is established, successfully.")

while True:
    server_message = client_socket.recv(1024).decode('utf-8')
    print("SERVER: ", server_message)
    if server_message.strip() == "Server disconnected successfully.":
        #here, thing to note is, .strip() won't really, remove the spaces inside the string, but just the stuffs outside and before.
        break
    #Now, user sends the request method.
    req_method_input = input("Specify the method of request ['GET', 'POST', 'PUT', 'DELETE'] or ['STOP']: ")
    req_method = req_method_input.upper().strip()

    #The request methods are sent to the server.
    client_socket.send(req_method.encode('utf-8'))

    #The server has to receive this request.
    server_response = client_socket.recv(1024).decode('utf-8')
    print("Server's response: ", server_response)

    if req_method == "STOP":
        break

print("Server Disconnected.")
client_socket.close()