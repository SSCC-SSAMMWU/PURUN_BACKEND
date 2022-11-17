import serial

py_serial = serial.Serial(
    port='COM9',
    baudrate=9600,
)

while True:
    with open("arduino_test.txt", "r") as file:
      for line in file.readlines():
        ans = line
    if ans == "on":
        commend = 'a'
    elif ans == "off":
        commend = "b"
    py_serial.write(commend.encode())
    if py_serial.readable():
        # 들어온 값이 있으면 값을 한 줄 읽음 (BYTE 단위로 받은 상태)
        # BYTE 단위로 받은 response 모습 : b'\xec\x97\x86\xec\x9d\x8c\r\n'
        response = py_serial.readline()
        # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
        print(response.decode().strip())
        k = "on".encode()
        if (k in response) :
             with open("arduino_test.txt", "w", encoding = "utf8") as report_file:
                report_file.write("off")