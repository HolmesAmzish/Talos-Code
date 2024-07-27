import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        # wating for connection
        conn = sock.accept()
        data = conn.recv(1024)
        print(data)

        # return connection information
        conn.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send("Successful connection!".encode("utf-8"))

        # close connection
        conn.close()

if __name__ == "__main__":
    main()