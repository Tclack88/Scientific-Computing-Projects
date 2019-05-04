#!/bin/bash

#purpose: basic .sh webscrape to find a last update on a class website

wget -q -O- web.physics.ucsb.edu/~phys129/lipman | grep update \
| sed -e 's/<[^>]*>//g'

						# wget downloads files from the web. In this case, a 
						# website is specified and it will create a local copy
						# of that website (which is just an html file)
						# the option -q is "quiet", this removes all the
						# extraneous output, like the download location and
						# all the progress updates
						# this is then piped to the grep command, which will
						# search for any line that has "update" in it
						#
						# The basic syntax of sed 's/STUFF/OTHERSTUFF/g' will 
						# search and replace any instance of STUFF and replace
						# it with OTHERSTUFF. g applies this globally (i.e. not
						# just to the first instance, which is the default)
						# looking at the HTML file ahead of time I see:
						# latest update: <some stuff> date <other stuff>
						# so I want to find any instances of anything between
						# two angle brackets < > and replace it with ... nothing
						# i.e. delete it
						# the <[^>]*> accomplishes this. Here's how:
						# [...] is a character class (e.g. [0-9] is for numbers) 						# the ^ means "not" so sed will read this as:
						# " look for a '<' then grab anything (*) that's not
						# a '>' ([^>])... Then replace all that with a blank."
						# NOTE: All this extra work, rather than the simpler:
						# <.*> is necessary. It prevents sed from eliminating 
						# EVERYTHING between the angle  brackets, including 
						# the date we want to keep.
