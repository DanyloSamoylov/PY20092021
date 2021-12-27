from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(('localhost', 8000))

try:
    while True:
        msg = input('Write any text: ')
        if msg == 'quit' or msg == 'exit':
            tcp_socket.close()
            break
        tcp_socket.send(msg.encode())
        server_resp = tcp_socket.recv(1024)
        print(server_resp.decode())
finally:
    tcp_socket.close()

