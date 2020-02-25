#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# Commands: https://dl-cdn.ryzerobotics.com/downloads/tello/0228/Tello+SDK+Readme.pdf
# 1/1/2018

import threading
import socket
import sys
import time
from controller import Controller
from input_handler import InputHandler

host = '192.168.10.2'
port = 9000
locaddr = (host,port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

command_address = ('192.168.10.1', 8889)

sock.bind(locaddr)



print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
#recvThread = threading.Thread(target=recv)
#recvThread.start()

controller = Controller(sock, command_address)
ih = InputHandler(controller)


camera_address = ('0.0.0.0', 11111)

cam_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



"""

while True:

    try:
        msg = input("");

        if msg == '1':
            controller.takeoff()
        if msg == '2':
            controller.land()

        if not msg:
            break

        if 'end' in msg:
            print ('...')
            sock.close()
            break 

        # Send data
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, tello_address)

    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
"""