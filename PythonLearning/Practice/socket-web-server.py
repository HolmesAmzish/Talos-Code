import socket

def start_server(host='0.0.0.0', port=8000):
    # 创建一个socket对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定服务器的地址和端口
        s.bind((host, port))
        # 开始监听传入的连接
        s.listen()
        print(f'Server listening on {host}:{port}...')
        
        while True:
            # 接受一个连接
            conn, addr = s.accept()
            with conn:
                print(f'Connected by {addr}')
                while True:
                    # 接收客户端的数据
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f'Received: {data.decode()}')

                    # 构建HTTP响应
                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        "Connection: close\r\n\r\n"
                        "<html><body><h1>Successful connection!</h1></body></html>"
                    )
                    conn.sendall(response.encode("utf-8"))
                    break  # 发送响应后退出循环，以关闭连接

if __name__ == '__main__':
    start_server()
