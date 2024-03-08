import socket

# 서버의 호스트 이름과 포트 번호를 정의합니다.
SERVER_IP = '166.104.246.42'
PORT = 12400

def main():
    # UDP 소켓 객체를 생성합니다.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        try:
            # 사용자로부터 데이터 길이를 입력받습니다.
            message_length = int(input("요청할 데이터의 길이를 입력하세요: "))
            
            # 서버에 전송할 메시지를 준비합니다. (여기서는 길이 정보를 문자열로 전송)
            message = str(message_length).encode('utf-8')
            
            # 메시지를 서버로 전송합니다.
            client_socket.sendto(message, (SERVER_IP, PORT))
            
            # 서버로부터 응답을 받습니다.
            data, _ = client_socket.recvfrom(1472)  # 버퍼 크기를 1472로 설정
            
            # 받은 데이터를 출력합니다.
            print(f"서버로부터 받은 데이터: {data.decode('utf-8')}")
        except ValueError:
            print("유효한 숫자를 입력해야 합니다.")
        except Exception as e:
            print(f"에러 발생: {e}")

if __name__ == "__main__":
    main()

