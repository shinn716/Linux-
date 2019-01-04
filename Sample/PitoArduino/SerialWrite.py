import pygame, sys
import time
import serial
from pygame.locals import *

ser = serial.Serial("COM3", baudrate = 9600, timeout = 3.0)      # Windows COM3          Linux /dev/ttyUSB0

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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            ser.close()
        if event.type == KEYDOWN:
            key = event.key
            if key == pygame.K_q:  
                data = 'q' 
                ser.write(data.encode())
                time.sleep(1)
            if key == pygame.K_w:   
                data = 'w' 
                ser.write(data.encode())
                time.sleep(1)
            if key == pygame.K_e:
                data = 'e' 
                ser.write(data.encode())
                time.sleep(1)
                
            if key == pygame.K_r:
                data = 'r' 
                ser.write(data.encode())
                time.sleep(1)
            if key == pygame.K_t:
                data = 't' 
                ser.write(data.encode())
                time.sleep(1)
            if key == pygame.K_y:
                data = 'y' 
                ser.write(data.encode())
                time.sleep(1)
            if key == pygame.K_u:
                data = 'u' 
                ser.write(data.encode())
                time.sleep(1)