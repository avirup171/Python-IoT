import serial
import time

ser = serial.Serial(port='/dev/cu.usbserial-1240',baudrate=9600)

switchOn="1"
switchOff="2"

while True:
    ser.write(bytes(switchOn,'utf-8'))
    time.sleep(1)
    ser.write(bytes(switchOff,'utf-8'))
    time.sleep(2)