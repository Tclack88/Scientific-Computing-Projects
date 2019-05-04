#!/usr/bin/python3

# The purpose of this program is to prime factor a number given an input
number = input("Please enter a positive integer here to be prime factorized: ")


while number.isdigit() is False:
  
  print("Not an integer...")
  number = input("Try again: ")
								# While loops go until it's output is True
								# however I choose to make if be False
								# so if the given input is not an integer
								# this has the effect of prompting the user
								# until an integer is given  
n = int(number)
						
								# input is usually just a string, it must
								# be converted to an integer for operation
								# relabel as n for readability
while n % 2 == 0:
  print(2)
  n = n//2
								# As Lipman hinted, getting rid of any 2's
								# will dramatically drop the overall number
								# and as many times as the numbe is divisible
								# by 2 this while loop will print 2
								# NOTE: I chose to print ALL prime factors
								# even if they repeat. Nothing in the prompt
								# suggested this was undesired								

for i in range (3, int(n**.5)+1,2):
  while n % i == 0:
    print (i)
    n = n //i
								# Brute force. Now if the number is divisible
								# evenly by any number, that number is a factor
								# the end of the "while loop" extracts that
								# digit (n//i). The next time that digit comes
								# up again, it will be reprinted (i.e. returns
								# degenerate factors). The "for loop" begins
								# at 3 since the previous step removes all
								# 2's. And no other even number is prime, so
								# this cuts the number of steps to check in half
								# Finally, the smallest number of primes a
								# number can be composed of is two, and at most
								# those two numbers could be the same number
								# so it suffices only to check up to the square									# root of the number given.
if n>1:
	 print (n)
								# any remaining numbers (if not 1) must be
								# prime (by the prime number theorem, any
								# number can be expressed as a product of 
								# primes) so it gets printed
