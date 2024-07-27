"""
program: socket-server.py
date: 2024.07.27
author: nulla
"""

import socket

def start_server(host='localhost', port=8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        print(f'Server listening on {host}:{port}...')

        # Accept a connection
        conn, addr = sock.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'Received: {data.decode()}')
                conn.sendall(data)

if __name__ == '__main__':
    start_server()