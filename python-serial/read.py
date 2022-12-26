import serial

ser = serial.Serial(port='/dev/cu.usbserial-0001',baudrate=9600)

while(1):
    x=ser.readline()
    print(str(x,'UTF-8'))


