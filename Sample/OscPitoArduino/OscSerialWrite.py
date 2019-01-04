import argparse
import math
import pygame, sys
import time
import serial

from pythonosc import dispatcher
from pythonosc import osc_server
from pygame.locals import *

ser = serial.Serial("COM5", 9600, timeout=3)                    # Windows COM3          Linux /dev/ttyUSB0

if ser.isOpen:
    ser.close()
ser.open()
ser.isOpen()

def print_volume_handler(unused_addr, args, volume):
    # print("[{0}] ~ {1}".format(args[0], volume))
    if args[0] == '/data':
        if volume == 0:
            data = 'q' 
            print("Receive q")
            ser.write(data.encode())
        elif volume == 1:
            data = 'w' 
            print("Receive w")
            ser.write(data.encode())
        elif volume == 2:
            data = 'e' 
            print("Receive e")
            ser.write(data.encode())
 

if __name__ == "__main__":


    try:
        print("Game Start")
        # Shinn OSC Receiver
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
        parser.add_argument("--port", type=int, default=5005, help="The port to listen on")
        args = parser.parse_args()

        dispatcher = dispatcher.Dispatcher()
        dispatcher.map("/data", print_volume_handler, '/data')

        server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)

        print("Serving on {}".format(server.server_address))    
        server.serve_forever()
    
    except KeyboardInterrupt:
        sys.exit(0)
        ser.close()
        


