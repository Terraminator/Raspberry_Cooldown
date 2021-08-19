from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import time
import os

normal = 30
warm = 35
high = 40
veryhigh = 45

cpu = CPUTemperature()

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.LOW)

while True:
	cpu = CPUTemperature()
	if cpu.temperature >= veryhigh or cpu.temperature == veryhigh:
		GPIO.output(17, GPIO.HIGH)
		os.system("sudo shutdown -h 0")
	elif cpu.temperature >= high or cpu.temperature == high:
		GPIO.output(17, GPIO.HIGH)
	elif cpu.temperature <= hoch and cpu.temperature >= warm:
		GPIO.output(17, GPIO.HIGH)
	elif cpu.temperature <= normal or cpu.temperature == normal:
		GPIO.output(17, GPIO.LOW)
	elif cpu.temperature <= warm or cpu.temperature == warm:
		GPIO.output(17, GPIO.LOW)
	time.sleep(1)
GPIO.cleanup()
