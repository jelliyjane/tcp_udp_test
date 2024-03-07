# client.py
import http.client
import time

# 외부 서버의 IP 주소와 포트 번호 설정
SERVER_IP = '211.252.176.35'  # 외부 서버의 실제 IP 주소로 변경
PORT = 12400

# 서버에 HTTP GET 요청 보내기
conn = http.client.HTTPConnection(SERVER_IP, PORT)
conn.request("GET", "/random")
start = time.time()
res = conn.getresponse()
end = time.time()
print(f"{end - start:.5f} sec")
# 서버로부터 받은 응답 출력
print("Response status:", res.status, res.reason)
data = res.read()
print("Received data:", data.decode("utf-8"))
