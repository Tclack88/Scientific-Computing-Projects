#!/usr/bin/python3

# PURPOSE: open a server on localhost to listen for a connection, when a connection is 
# made, the server side will indicate this as well as the local time

import socket
import time

TimeOfDay = time.strftime("%I:%M %p")
host = ''
port = 55555

								# Host is left blank, which means its sort of 
								# a blank slot to accept all interfaces. Time
								# of day and port number will be called later.

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

								# Etablish a TCP socket connection
								# AF_INET - Address family
								# SOCK_STREAM - internet, not UDP


s.bind((host,port))

								# Connect the host to the port (via the socket) 

s.listen(1)
conn, addr = s.accept()

								# listens for a connection request. the '1'
								# in the argument is a queue, establishing how
								# many requests will be accepted before any
								# more are turned away. (Only need one for the
								# sake of this problem). Then the connection is									# accepted


print ("\nConnection successful\nCurrent time:",TimeOfDay,"\n")

