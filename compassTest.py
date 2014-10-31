import pynmea2
import serial

ser = serial.Serial()
ser.baudrate = 4800
ser.port = '/dev/ttyAMA0'
ser.bytesize = 8
ser.parity = 'N'
ser.stopbits = 1
ser.xonxoff = 0
ser.rtscts = 0
ser.timeout=2
ser.open()
ser.flushInput()

streamreader = pynmea2.NMEAStreamReader()

while 1:
	try:
		line = ser.readline()
		#print line
	except serial.serialutil.SerialException:
		pass
	if line.startswith('$'):
		for msg in streamreader.next(line):
			if msg.sentence_type == 'HDG':
				print msg.heading
