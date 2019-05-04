#!/usr/bin/python3

#purpose: basic .py webscrape to find a last update on a class website using bs4 library

import requests 
from bs4 import BeautifulSoup

	    	# BeautifulSoup is used for pulling data from HTML ir XML files
		# requests is an improved HTTP library for very simply sending
		# HTTP/1.1 requests 

source = requests.get('http://web.physics.ucsb.edu/~phys129/lipman/').text
	
		# grabs the html source code as text from the specified website
		# assign it to the variable 'source'


soup = BeautifulSoup(source, 'html.parser')
	
		# It's standard to name this variable soup, but all we do here
		# is apply Beautiful soup to the source code. Beautiful soup
		# breaks it all up into just 4 objects. (Tags, Navigablestrings,
		# BeautifulSoups and comments). In this case, the HTML tags 
		# (such as <p> ... </p>) is all we need to deal with.

line = soup.find('p')

		# The find() method searches those 4 objects described above
		# Here, I'm finding the <p> tag
		# The <p> tag only appears once, so fortunately, this
		# simplified the tag I need to search out

date = line.span.text

		# Nested within the <p> tag is a <span> tag (which I suppose
		# you can think of span having some test nested within it)
		# So all that nesting here is assigned to the variable 'date'

print ('Latest update:',date)

