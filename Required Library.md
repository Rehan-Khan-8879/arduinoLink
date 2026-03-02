pip install pyserial
example code:


import serial

# CHANGE COM PORT HERE
ser = serial.Serial('COM5', 9600, timeout=1)

print("Listening to ESP8266...\n")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print(line)
