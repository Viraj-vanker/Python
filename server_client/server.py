import socket
def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host,port))

    server_socket.listen(5)
    print(f"server listening on {host}:{port}...")

    client_socket, client_address = server_socket.accept()
    print(f"connection from {client_address} has been established.")

    while True:
        data=client_socket.recv(1024)
        if not data:
            break
        print(f"received message: {data.decode()}")
        client_socket.sendall(data)
    client_socket.close()
    print("connection closed.")
if __name__=='__main__':
    start_server()