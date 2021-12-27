"""
Echo server with threading

Create a socket echo server which handles each connection in a separate Thread
"""
from socket import *
import threading


def listen_for_new_client(connection, address):
    try:
        print('Connected', address)
        while True:
            with connection:
                client_msg = connection.recv(1024).decode()
                print(f'{threading.current_thread().getName()} info. recived: {client_msg}')
                if client_msg == 'quit':
                    connection.send(client_msg.encode())
                    connection.close()
                    break
                print(addr, ': ', client_msg)
                connection.send(client_msg.encode())
    finally:
        connection.close()


HOST = '127.0.0.1'
PORT = 8000

tcp_socket = socket(AF_INET, SOCK_STREAM)
try:
    tcp_socket.bind((HOST, PORT))
    tcp_socket.listen(2)
    while True:
        conn, addr = tcp_socket.accept()
        threading.Thread(target=listen_for_new_client, args=(conn, addr)).start()
finally:
    tcp_socket.close()
