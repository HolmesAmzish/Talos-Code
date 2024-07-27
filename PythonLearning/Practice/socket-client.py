import socket

def start_client(host='127.0.0.1', port=65432):
    # 创建一个socket对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到服务器
        s.connect((host, port))
        # 发送数据
        s.sendall(b'Hello, world')
        # 接收服务器的响应
        data = s.recv(1024)
        print(f'Received from server: {data.decode()}')

if __name__ == '__main__':
    start_client()
