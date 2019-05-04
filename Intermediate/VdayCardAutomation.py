#!/usr/bin/python3

with  open('classlist.csv') as classlist:	# with is necessary for "open as" 
											# function to work. It has the
											# additional benefit of															# automatically closing the file
											
	for line in classlist:											# 1
		student = line.split(',')									# 2
		last_name = student[0].capitalize()							# 3
		first_name  = student[1].split(' ')							# 4
		first_name = first_name[0].capitalize()						# 5
		print ("Happy Valentine's Day,",first_name,last_name+"!")	# 6

			#1 open a for loop where each element I am calling 'line'
			#  (I tested out the file before hand by printing i for i in f
			#  So I suppose each line is automatically an element of a 
			#  CSV file.. I wouldn't have known this without that test)
			#2 Separate lists called 'student' that contains all the info
			#  of each line split by commas
			#3 Peeking at the CSV file, the first element was the last name
			#  so it was of course element 0 of 'student'. capitalize() is a
			#  convenient function that puts the word into the desired format
			#4 As in 3, but it contained middle names. To get the first word
			#  of that list (i.e. the first name) I split again by spaces
			#5 redefine first_name as just the 1st element of that list
			#6 concatenate the above. By default, commas in print automatically 
			#  add space space, '+' will conjoin them without spaces

