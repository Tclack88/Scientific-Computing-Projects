#!/usr/bin/python3

# The purpose of this program is to take info from a .csv file (csv.csv... very creative name)
# and automate the process of finding specific information:


import csv


with open('csv.csv') as f:
	readCSV = csv.reader(f, delimiter=',')
						# "with open(file) as f" automatically closes after
						# the operation is complete. rename to f for ease
						# of typing. csv.reader returns an object in the file
						# (separated by commas)
	people = []
					# create a blank list to while I will append dictionaries


	for person in readCSV:

		people.append({'last':person[0],'first':person[1],'color':person[2], \
					'food':person[3],'field':person[4],'physicist':person[5]})

						# Creates a dictionary for each row in the file
	

	print("I have information here about a bunch of people:\n")

	response = 'y'
	while response == 'y':

		print(list(people[0].keys()))
		choice = input("What would you like to know about? ")

		print()

							# This while loop sets up the requirement to
							# continue to prompt the user for keys
		people_sort = []

		for person in people:
			item =(person['last']+", "+person['first']+": "+person[choice])
			people_sort.append(item)
		people_sort = sorted(people_sort)

							# blank list people_sort is for the alphabetizing
                            # of the output. The key choice is will put the
							# string "Last, first: key" for each row and store
							# that into the blank list which is default sorted
							# alphabetically

	
		for i in people_sort:
			print(i)
		print()
							# Here we print the already sorted list
							
		response = input("Would you like to know more? <y,n> ")	
		if response == 'n':
			break
		while response != 'n' and response !='y':
			print("That's not a valid response, try again")
			response = input("Would you like to know more? <y,n> ")
	
							# Here is where the user is prompted if they'd
							# like to continue. I do a few short while loops
							# to ensure only "y" or "n" is input



"""            THE FOLLOWING DOES PART OF THE TASK, BUT DOESN'T USE 
				THE DICTIONARY AS REQUESTED... I'M KEEPING IT HERE
				BECAUSE I'M PROUD OF IT AND MAY WANT TO REFER BACK
				TO IT LATER

import csv


with open('csv.csv') as f:
    readCSV = csv.reader(f, delimiter=',')

    print("I have here a list of people, their first names, last names, \
            favorite color, food, field of physics and physicist.\n")
    choice = input ("Which would you like to know? last, first, color, \
                    food, field.\n (type one):")

    last = []
    first = []
    color = []
    food = []
    field = []
    physicist = []

    for row in readCSV:

        last = row[0]
        first = row[1]
        color = row[2]
        food = row[3]
        field = row[4]
        physicist = row[5]


        print(last+","+first+":"+choice)
"""
