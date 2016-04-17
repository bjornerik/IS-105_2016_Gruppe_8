"""Deler av koden er hentet fra http://www.binarytides.com/programming-udp-sockets-in-python"""

import socket 
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = 'localhost';
port = 8888;

#initiating communication with the server
print "Type anything to start the game"

while(1) :
    #looping for commands
    msg = raw_input(">")

    s.sendto(msg, (host, port))

    # receive data from server (data, addr)
    d = s.recvfrom(1024)
    reply = d[0]
    addr = d[1]

    #No feedback is the server's way of telling that the game is over
    #if not reply:
        #print 'Game is over'
        #break

    print reply
