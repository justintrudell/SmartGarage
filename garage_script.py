#!/usr/bin/python
import os
import RPi.GPIO as GPIO
from time import sleep

SWITCH = 14
DIST = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.OUT)
GPIO.setup(DIST, GPIO.IN)
GPIO.output(SWITCH, GPIO.LOW)

while(True):
	os.system("sudo php garage_php.php")
	file = open('garage_output.txt', 'r')
	str = file.read()
	output = str.split(';')
	number = output[0]
	message = output[1]
	status = GPIO.input(DIST)
	if "check" in  message.lower().strip():
		if status == 0:
			command = "garage_closed.txt"
		else:
			command = "garage_opened.txt"
	elif "close" in message.lower().strip() == "close":
		if status == 1:
			command = "garage_closing.txt"
			GPIO.output(SWITCH, GPIO.HIGH)
			sleep(2)
			GPIO.output(SWITCH, GPIO.LOW)
		else:
			command = "garage_already_closed.txt"
	elif "open" in message.lower().strip() == "open":
		if status == 0:
			command = "garage_opening.txt"
			GPIO.output(SWITCH, GPIO.HIGH)
			sleep(2)
			GPIO.output(SWITCH, GPIO.LOW)
		else:
			command = "garage_already_open.txt"
	elif "kill" in message.lower().strip() == "kill":
		break
	else:
		command = "garage_error.txt"
	os.system("mail %s < %s" % (number, command))
