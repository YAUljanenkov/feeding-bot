isfeeded = {}
from datetime import datetime
import serial
import time


ardu = serial.Serial('/dev/cu.usbmodem1411')
ardu.baudrate = 9600


while True:
    nowadays = datetime.strftime(datetime.now(), "%H:%M")

    myfile = open('list.txt')
    a = myfile.read()

    if a.find(nowadays) !=-1:
        ardu.write(b'1')
        time.sleep(60)
    myfile.close()





