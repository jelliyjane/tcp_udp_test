import socket
import time
import csv

SERVER_IP = '127.0.0.1'  # 서버의 실제 IP 주소로 변경해야 합니다.
SERVER_PORT = 8000

def send_udp_data(sock, server_address, size):
    data = b'x' * size
    start_time = time.time()
    sock.sendto(data, server_address)
    print("odododo")
    sock.settimeout(2.0)  # 2초 동안 응답을 기다립니다.
    try:
        received, _ = sock.recvfrom(4096)
        end_time = time.time()
        return end_time - start_time
    except socket.timeout:
        print("Response timed out")
        return None

def main():
    window_sizes_kb = [4, 16, 64, 128, 1024]
    iterations = 30
    results = {size: [] for size in window_sizes_kb}
    server_address = (SERVER_IP, SERVER_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        for size in window_sizes_kb:
            print(f"Testing with window size: {size}K")
            for _ in range(iterations):
                elapsed_time = send_udp_data(sock, server_address, size * 1024)
                if elapsed_time is not None:
                    results[size].append(elapsed_time)
                    print(f"Elapsed time: {elapsed_time:.5f} seconds")
                    time.sleep(2)
                else:
                    print("Test failed due to timeout.")
   
    # 결과 정렬 및 저장
    for size in window_sizes_kb:
        results[size].sort()

    with open('udp_test_results.csv', 'w', newline='') as csvfile:
        fieldnames = [f"{size}K" for size in window_sizes_kb]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(iterations):
            row = {f"{size}K": results[size][i] if i < len(results[size]) else "" for size in window_sizes_kb}
            writer.writerow(row)

if __name__ == "__main__":
    main()