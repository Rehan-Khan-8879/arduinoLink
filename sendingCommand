import time 
import serial

arduino = serial.Serial(port='COM2',baudrate=9600,timeout=1)
checksum = 0
while True:
    if checksum == 1:
        break
    while checksum ==0:
        data = input("write something here ")
        if data == "exit":
            checksum =1
            break
        arduino.write(data.encode())
        time.sleep(1)
        val = arduino.readline().decode().strip()
        print("Arduino has revived ",val)
