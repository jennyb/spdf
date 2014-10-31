#!/usr/bin/python
import sys
import argparse
import getopt
import serial
import time
from bitstring import BitArray
from time import sleep

bcda0 = 3   #BCD0 
bcda1 = 5   #BCD1 
bcda2 = 7   #BCD2 
bcda3 = 11  #BCD3

bcdb0 = 13  #BCD0  
bcdb1 = 15  #BCD1 
bcdb2 = 19  #BCD2
bcdb3 = 21  #BCD3 


bcdc0 = 23  #BCD0  
bcdc1 = 22  #BCD1 
bcdc2 = 24  #BCD2 
bcdc3 = 26  #BCD3 

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

def main():
	#parser = argparse.ArgumentParser()
	#parser.add_argument('-d', dest='device', action='store', default="/dev/ttyAMA0", help="Serial device path", required=True)
	#parser.add_argument('-o', dest='output', action='store', default=None, help="Output file", required=False)
	#parser.add_argument('-s', dest='stdout', default=1, required=False, help="Print output to stdout")
	#args = parser.parse_args() 

	#if args.device == None:
	if 1:
 		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(bcda0,GPIO.IN)  #AZ0 Red    BCD0 
		GPIO.setup(bcda1,GPIO.IN)  #AZ1 Blue   BCD1
		GPIO.setup(bcda2,GPIO.IN)  #AZ2 Green  BCD2
		GPIO.setup(bcda3,GPIO.IN)  #AZ3 Yellow BCD3
		
		GPIO.setup(bcdb0,GPIO.IN)  #AZ0 Red    BCD0 
		GPIO.setup(bcdb1,GPIO.IN)  #AZ1 Blue   BCD1
		GPIO.setup(bcdb2,GPIO.IN)  #AZ2 Green  BCD2
		GPIO.setup(bcdb3,GPIO.IN)  #AZ3 Yellow BCD3
		
		GPIO.setup(bcdc0,GPIO.IN)  #AZ0 Red    BCD0 
		GPIO.setup(bcdc1,GPIO.IN)  #AZ1 Blue   BCD1
		GPIO.setup(bcdc2,GPIO.IN)  #AZ2 Green  BCD2
		GPIO.setup(bcdc3,GPIO.IN)  #AZ3 Yellow BCD3
		
		
		digit1 = 0
		digit2 = 0
		digit3 = 0

		while (1):
			bcd = BitArray('0b0000')
			if GPIO.input(bcda0):
				bcd.invert(3)
			if GPIO.input(bcda1):
				bcd.invert(2)
			if GPIO.input(bcda2):
				bcd.invert(1)
			if GPIO.input(bcda3):
				bcd.invert(0)
			digit1=bcd.uint
			if digit1 > 9:
				digit1=0

			bcd = BitArray('0b0000')
			if GPIO.input(bcdb0):
				bcd.invert(3)
			if GPIO.input(bcdb1):
				bcd.invert(2)
			if GPIO.input(bcdb2):
				bcd.invert(0)
			if GPIO.input(bcdb3):
				bcd.invert(1)
			digit2=bcd.uint
			if digit2 > 9:
				digit2=0
		
			bcd = BitArray('0b0000')
			if GPIO.input(bcdc0):
				bcd.invert(3)
			if GPIO.input(bcdc1):
				bcd.invert(2)
			if GPIO.input(bcdc2):
				bcd.invert(0)
			if GPIO.input(bcdc3):
				bcd.invert(1)
			digit3=bcd.uint
			if digit3 > 9:
				digit3=0

			bearing = digit1*100 + digit2*10 + digit3
			print bearing

	else:
		print ("Too many parameters")
		parser.print_help()
    
if __name__ == '__main__':
		main() 

