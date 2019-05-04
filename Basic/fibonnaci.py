#!/usr/bin/python3

# The purpose of this program is to list the first n digits of the fibonnaci numbers.
# A cap is placed at 75 characters, because  default terminal size is about 80 characters
number = input("Give me an integer: ")
						

while number.isdigit() is False or number == '0':
	number = input("Sorry, not a valid integer. Try again: ")
							
							# This very clever while loop I came up with will
							# only accept integer inputus.
							# Shoutout to Shahryar for finding that my code 
							# originally didn't account for '0' so I fixed that	

number = int(number)

def fib(n):

	a = 1
	b = 1
	print (1)

	for i in range(1,n):	
		if len(str(b)) <= 75:
			print(b)
		else:
			print("\n...I'm gonna stop here, number of output digits" \
					" exceeds 75\n")
			break
		a, b = b, b + a
					
							# The idea of this is as simple as the fib. seq.
							# itself. The first digit is 1, so I print that,
							# then a loop begins wherein b is printed, then a
							# is reassigned to "b" and b is reassigned to 
							# "a + b". Doing this simultaneously ensures we 
							# don't "double add b" or anything. I put this in								# a "for loop" so it will go up to the asked digit
							# 
							# a nest "if statement" will ensure it prints only
							# digits with length < 75 digits. Then break the
							# "for loop" so it doesn't continue running up the
							# range

fib(number)

							# run the function
