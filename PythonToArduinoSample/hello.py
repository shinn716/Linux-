import pygame, sys
import time
import serial
from pygame.locals import *
#import RPi.GPIO as GPIO

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(26, GPIO.OUT)
#GPIO.output(26, GPIO.LOW)


ser = serial.Serial(
    "/dev/ttyUSB0",
    baudrate = 9600,
    timeout = 3.0
)

print("Game Start")


if ser.isOpen:
    ser.close()
ser.open()
ser.isOpen()


pygame.init()
BLACK = (0,0,0)
WIDTH = 100
HEIGHT = 100
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
windowSurface.fill(BLACK)
x = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            ser.close()
        if event.type == KEYDOWN:
            key = event.key
            if key == pygame.K_q:   
		print("q")
                ser.write('q')
            if key == pygame.K_w:   
		print("w")
                ser.write('w')
            if key == pygame.K_e:
		print("e")
                ser.write('e')
            if key == pygame.K_r:
                ser.write('r')
            if key == pygame.K_t:
                ser.write('t')
            if key == pygame.K_y:
                ser.write('y')
            if key == pygame.K_u:
                ser.write('u')
