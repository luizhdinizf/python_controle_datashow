import serial 
import struct
import time
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
) 

ligar = False
print(ser.isOpen())
start = "\xA9"
item1 = "\x17"
if ligar == True:
	item2 = "\x2E"
else:
	item2 = "\x2F"
set_get = "\x00"
data1 = "\x00" 
data2 = "\x00"
check = "\x3F"
end = "\x9A"
#thestring = "7E FF 03 00 01 00 02 0A 01 C8 04 D0 01 02 80 00 00 00 00 8E E7 7E"
data = start + item1 + item2 + set_get + data1+data2+check+end
print str(data)
#data = struct.pack(hex, 0x7E, 0xFF, 0x03, 0x00, 0x01, 0x00, 0x02, 0x0A, 0x01, 0xC8,      0x04, 0xD0, 0x01, 0x02, 0x80, 0x00, 0x00, 0x00, 0x00, 0x8E, 0xE7, 0x7E)

ser.write(data)


time.sleep(1)
#s = ser.read(1)
#print(s)
ser.close()
exit()