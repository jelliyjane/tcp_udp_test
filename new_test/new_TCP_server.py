import http.server
import socketserver
import random
import string
import socket
import sys

SERVER_IP = '192.168.0.199'
PORT = 12403
rtt_count = 0  # Initialize counter to track RTT count
LENGHT = 23556
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        rtt_count = 0
        if self.path == '/random':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            # Generate random data based on user input length
            random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            self.wfile.write(random_data.encode('utf-8'))

            # Increase RTT count each time a request is processed
            rtt_count += 1
            print(f"Total number of RTTs: {rtt_count}")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

#def set_congestion_control_algorithm(sock):
    # Set TCP congestion control algorithm to Cubic
   # sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_CONGESTION, b'cubic')

def set_receive_window_size(sock, size):
    # Set receive window size
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, size)

if __name__ == "__main__":
    # Check if the length argument is provided
    #if len(sys.argv) < 2:
    #    print("Usage: python3 script.py <length>")
    #    sys.exit(1)

    # Get the length from command-line argument
    length = LENGHT

    # Create TCP server
    with socketserver.TCPServer((SERVER_IP, PORT), MyHandler) as httpd:
        print(f"Server started on {SERVER_IP}:{PORT}")

        # Configure congestion control algorithm for each connection
        httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 #       set_congestion_control_algorithm(httpd.socket)

        # Process requests infinitely
        httpd.serve_forever()

