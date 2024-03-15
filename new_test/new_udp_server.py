import socket
import os

def server():
    SERVER_IP = '127.0.0.1'  # 실제 서버 IP로 변경해야 함
    SERVER_PORT = 8000

    server_address = (SERVER_IP, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(server_address)
        print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

        while True:
            data, address = sock.recvfrom(4096)
            if data:
                size = int(data.decode())
                print(f"server send {size}bytes to client in UDP")
                random_data = os.urandom(size)
                sock.sendto(random_data, address)

if __name__ == "__main__":
    server()
