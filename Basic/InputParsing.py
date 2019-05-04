#!/usr/bin/python3

words = input ("Hi, go ahead and write something, at least 3 words long: ")

    					 # .split() stops any tomfoolery if someone
						 # tries to "beat the system" by assuming a
						 # word is defined by number of space characters

while len(words.split()) < 3:
  words = input ("Can you read? At least three words, bruh. Try again: ")
		    # if the length of the list generated (post split)
                    # then it will reprompt until the input meets or
                    # exceeds 3 words. (If I used 'if', it would
		    # only prompt once) 

  wordsmod = words.split() 
		    # This is needed for individual manipulation of
		    # words...It also catches aforementioned tomfoolery

print("\nAll words split:") 
		    # \n is interpreted as a line. 
		    # Provided for output readability

for i in wordsmod:
  print (i)
  
print ("\nfirst three characters:")

print (words[0:3])

print ("\nlast three characters:")

print (words[-3:])

half = (len(words))//2  
							 # the //2 returns an integer value it                         					 # rounds down for odd numbers, so in                          					 # order to counter this I need to check                       					 # for this rounding in the next step


if len(words)%half != 0:
  half = half + 1
else:
  half = half
						# If the original input was odd length, then this 
						# will fix to round up. The reason we round up is 
						# to ensure slicing in the next step will include 
						# the middle boundary if the original input was 
						# an odd length
						


print ("\nfirst half of string:")

print (words[0:half])



print ("\nLast half of string:")

print (words[-(half):])


print ("\nwords in reverse order:")

print (' '.join(wordsmod[-1::-1]))
						 # Without ' '.join() function, this would return a 
						 # list of words but they wouldn't appear as a string


print ("\nwords alphabetized:")

print (' '.join(sorted(wordsmod))) 
						# sorted() alphabetizes a list. I again joined it
						#  with a space to avoid generating a list

print ("\neach character of the string by line:")

for i in (list(words)): 
  print (i)
					# list() makes a list from each character of its argument


  
print ("\neach character in unicode hexidecimal:")

for i in (list(words)):
  print (hex(ord(i)))
					# The same as above, but now for each character is first 
                    # converted to unicode then to hexidecimal


print ("\nDone!\n")
