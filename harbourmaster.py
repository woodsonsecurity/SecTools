#!/usr/bin/env python

# Habourmaster - Simple CLI Port Scanner
# Author: Michael Woods

# to run this script use the command line interface when in the script's directory:
# python harbourmaster.py <target IP Address> <starting port number> <ending port number>
# examples commands:
# python harbourmaster.py 192.168.1.10 0 1023 -> this command reports open well known ports
# python harbourmaster.py 192.168.1.10 1024 49151 -> this command reports open registered ports
# python harbourmaster.py 192.168.1.10 49152 65535 -> this command reports open dynamic ports

# Open ports will be printed to the screen

import sys, socket # importing the sys and socket python libraries

targetIP = sys.argv[1] # obtain target IP input argument from the command line instruction and assign to variable 1 tagetIP
startPort = int(sys.argv[2]) # obtain the starting port number from the command line instruction and assign to variable 2 startPort
endPort = int(sys.argv[3]) # obtain the last port number to scan from the command line instruction and assign to variable 3 endPort
# simple and accessible coding for this scanner, there are cleaner ways to obtain input but require more lines of code

def porttry(cur_target, port): # define a function port try with current target and port numnber
    try:
        s.connect((cur_target, port)) # If it connects without an error it returns true otherwise none
        return True
    except:
        return None

for i in range(startPort, endPort+1): # the for block scans the port numbers from the start to end defined range
    s = socket.socket(2, 1) #socket.AF_INET, socket.SCOK.STREAM
    value = porttry(targetIP, i) # on the target IP adddress scan port
    if value != None:
        print("Port open on %d" % i) # everything that is not none print open with the port number
