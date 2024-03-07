import socket
import threading
import os

def send_chunk(data, address):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(data, address)

def server():
    server_address = '127.0.0.1'
    server_port = 8000
    chunks = [os.urandom(1400) for _ in range(25)]  # Generates 25 chunks of 1200 bytes
    threads = []

    for chunk in chunks:
        thread = threading.Thread(target=send_chunk, args=(chunk, (server_address, server_port)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Total packets sent: {len(chunks)}")

if __name__ == "__main__":
    server()
