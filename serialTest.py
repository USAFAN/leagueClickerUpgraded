import serial
import time

ser =  serial.Serial('COM4', 9600) # Establish the connection on a specific port
time.sleep(2) # wait for the serial connection to initialize

while True:
    data = input("Enter a value between 1 and 100: ")
    if 1 <= int(data) <= 100:
        ser.write(str(data).encode())
    else:
        print("Invalid input. Enter a value between 1 and 100.")
