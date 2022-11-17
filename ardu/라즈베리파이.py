import serial

port = serial.Serial("/dev/ttyACOM0", "9600")

while True:
  try:
    data = port.readline()
    print("water_level: ")
    print(data)

  except KeyboardInterrupt:
    break
port.close()