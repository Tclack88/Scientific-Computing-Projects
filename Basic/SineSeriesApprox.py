#!/usr/bin/python3

import math
pi = 3.1415926535897932384626433832795028841971


def factorial(n):
  num = 1
  for i in range (1,n+1):
    num *= i
  return num
							# we are not allowed to import functions like
							# factorial or pi, so I have to define them here
							# Self explanatory definition I'd say 
  


angle= input("Give me an angle (in degrees): ")
							# Couldn't figure out how to make sure this is
							# either a float or integer... sorry
		
angle = float(angle)*pi/180

				
numterms = input("How many terms do you want? ")

while numterms.isdigit() is False or int(numterms)>=25:
	numterms = input("Don't be ridiculous. Only integers allowed" \
						" below 25, try again: ")
numterms = int(numterms)

						# The first while loop ensures only integer inputs are
						# accepted, the second keeps it below 25. Finally I 
						# turn the string input into an integer


def sind(angle,numterms):
	total = 0
	for i in range(1,numterms+1):
	  	n = ((-1)**(i-1))*((angle)**(2*i-1))/factorial((2*i-1))
  		total += n
	return total  
						# This is just the definition of sine as a taylor
						# expansion. Since we are adding terms up to a 
						# specified input, the "for i in range" works perfectly
						#
						# Note: initially I tried doing this as an array, but
						# my factorial definition only acts on single inputs
						# I'm not sure how to make it operate on arrays, so I
						# had to change to a range function


sind = sind(angle,numterms)
sin = math.sin(angle)
						# assign these variable names to the corresponding 
						# functions for simplicity

print ("\nHere is sind():\n",sind)

print ("\nHere is the math module's sine:\n",sin)


print("\nTo compare:\n\n The absolute difference is:\n", \
		math.sqrt((sin-sind)**2), \
		 "\n\nThe ratio is:(sind to sine)\n",sind/sin)

