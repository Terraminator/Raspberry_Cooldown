from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import time
import os

normal = 30
warm = 35
hoch = 40
ultrahoch = 45

cpu = CPUTemperature()

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.LOW)

while True:
	cpu = CPUTemperature()
	if cpu.temperature >= ultrahoch or cpu.temperature == ultrahoch:
		GPIO.output(17, GPIO.HIGH)
		os.system("sudo shutdown -h 0")
	elif cpu.temperature >= hoch or cpu.temperature == hoch:
		GPIO.output(17, GPIO.HIGH)
	elif cpu.temperature <= hoch and cpu.temperature >= warm:
		GPIO.output(17, GPIO.HIGH)
	elif cpu.temperature <= normal or cpu.temperature == normal:
		GPIO.output(17, GPIO.LOW)
	elif cpu.temperature <= warm or cpu.temperature == warm:
		GPIO.output(17, GPIO.LOW)
	time.sleep(1)
GPIO.cleanup()