import socket
import os
import random


def server():
    SERVER_IP = '172.31.21.125'  # 실제 서버 IP로 변경해야 함
    SERVER_PORT = 12460

    server_address = (SERVER_IP, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(server_address)
        print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

        while True:
            data, address = sock.recvfrom(4096)
            if data:
                size = int(data.decode())
                print(f"server send {size}bytes to client in UDP")
                random_data = ''.join(random.choices('0123456789abcdef', k=size))
                data = random_data.encode('utf-8')
               # random_data = os.urandom(size)
                sock.sendto(data, address)

if __name__ == "__main__":
    server()
