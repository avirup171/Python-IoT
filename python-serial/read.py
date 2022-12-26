import serial

ser = serial.Serial(port='/dev/cu.usbserial-0001',baudrate=9600)

while True:
    value= ser.readline()
    valueInString=str(value,'UTF-8')
    print(valueInString)