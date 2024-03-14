import socket

SERVER_IP = '172.31.21.125'
SERVER_PORT = 8000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((SERVER_IP, SERVER_PORT))
        print(f"UDP Server listening on {SERVER_IP}:{SERVER_PORT}")

        while True:
            data, addr = sock.recvfrom(4096)  # 최대 4096 바이트를 수신
            print(f"Received {len(data)} bytes from {addr}")

            # 클라이언트에게 응답 보내기
            if data:
                response = b"ACK"
                sent = sock.sendto(response, addr)
                print(f"Sent {sent} bytes back to {addr}")

if __name__ == "__main__":
    main()

