import socket

def client():
    client_address = '127.0.0.1'
    client_port = 8000
    received_packets = 0

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((client_address, client_port))
        sock.settimeout(10)  # Optional: set a timeout for receiving (e.g., 10 seconds)

        try:
            while True:
                data, addr = sock.recvfrom(1400)  # Buffer size is 1200 bytes
                if data:
                    received_packets += 1
        except socket.timeout:
            print("Receiving process timed out.")

    print(f"Total packets received: {received_packets}")

if __name__ == "__main__":
    client()
