#!/usr/bin/env python3

#purpose: .py webscrape to find a last update on a class website using tcp connections

import sys
import socket

def open_connection(ipn, prt):
   """Open TCP connection to ipnum:port.
   """
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
   s.connect_ex((ipn, prt))


   return(s)

						# This opens a TCP connection to the supplied ip
						# address and port number.
						# AF_INET specifies what socket type we want.
						# SOC_STREAM allows us to make a TCP connection.
						# The connect_ex() method returns a number 
						# corresponding to an error. If none exists a '0' is
						# returned. (This WILL be 0 because I remove user input
						# to the ip address and port number).


def receive_data(thesock, nbytes):
   """Attempt to receive nbytes of data from open socket thesock.
   """
   dstring = b''
   rcount = 0  # number of bytes received
   thesock.settimeout(5)
   while rcount < nbytes:
      try:
         somebytes = thesock.recv(min(nbytes - rcount, 2048))
      except socket.timeout:
         print('Connection timed out.', file = sys.stderr)
         break
      if somebytes == b'':
         break
      rcount = rcount + len(somebytes)
      dstring = dstring + somebytes

   return(dstring)

				
						# This function receives up to a specified number of 
						# bytes from the source. This prevents too much data
						# from being imported.
						# b'' is an empty byte string, the b in front of the
						# string, even though it displays characters, isn't a
						# unicode string, it's an "array of integers". This
						# serves the purpose of assigning the numerical size
						# value to the string.
						#
						# ::::The While loop above:::
						# Data will be recieved in chunks. Either in 2 kb 
						# chunks (1 kb = 1024 bytes) or the difference between 
						# the upper limit specified and the amount received, 
						# whichever is smaller. If that doesn't happen after 5
						# seconds, the attempt will time out and an error 
						# message will be displayed. If nothing is received,
						# then break the loop.

ipnum = "128.111.17.41"
port = 80
						# This is the ip adress and port number of the website
						# we wish to access. I'm providing it here as variables
						# and removing it from user input to minimize error
						# from proper user use
			

thesocket = open_connection(ipnum, port)

thesocket.send(b'GET /~phys129/lipman/ HTTP/1.0\r\n\r\n')
  
indata = receive_data(thesocket, 4096)
thesocket.shutdown(socket.SHUT_RDWR)
thesocket.close()

						# open the connection. Send a request for the specified
						# page, receive the data (as described above)
						# Then shutdown and close the connection

datastring = indata.decode()

						# turn the byte string into an actual mutable string

a = datastring.find('greenss">')
b = datastring.find('</span><')

						# These uniquely surround the string I'm interested in
						# So I set these as boundary points to slice from
						# find returns a number where the string given begins
						# Note that a starts 9 characters before the date
						# string I want to pull


print ('Latest update:',datastring[a+9:b])
						
						# print the slice of string I want (add the 9 to 'a'
						# to avoid printing 'greenss">')

