#!/usr/bin/python3	

# The purpose of this program is to calculate the number of days a person has been alive
# as well as the day they were born. This is done via Julian day rules

import re

def dateinput(message):
	InputDate = input(message)
	while re.match(r'^[0-9]{2}[A-Z]{1}[a-z]{2}[0-9]{4}',InputDate) is None:
		InputDate = input("Format does not match: Try again: ")
	return InputDate
								# I'm taking two inputs, one for today's date
								# and one for the birthdate, so the 'message'
								# is an input prompt for each of those later
								# 
								# This while loop checks the input matches
								# the required format. Shahryar informed me
								# of this re.match function

def parse(Date):

	months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,\
				'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

	DateList = []
	DateList.append(int(Date[0:2]))
	DateList.append(str(Date[2:5]))
	DateList.append(int(Date[5:]))


	DateList[1]=months[DateList[1]]

	return DateList

								# I made a dictionary relating each Mmm to the
								# corresponding day. Input string is expected
								# to be a string DDMmmYYY,so I grab the first
								# 2, the next 3 and the last 4 and append those
								# to a list (as integers or strings where 
								# called for. I take the second entry of the
								# DateList (entry [1]) and exchange it for the
								# corresponding integer in the months dictionary


def JulianDay(DateList):
	D = DateList[0]
	M = DateList[1]
	Y = DateList[2]

	if M <= 2:
		Y = Y - 1
		M = M +12

	A = int(Y/100)
	B = 2 - A + int(A/4)

	return int(365.25*(Y+4716)) + int(30.6001*(M+1)) + D +B -1524.5

					# This function operates on the output of the previous,
					# which is a list. After assigning each entry to D M Y
					# (for Day Month Year of course) I then blindly apply
					# The Julian day formula given in the handout. The
					# output of this function is the Julian day.
								


def DayOfWeek(JD):

	daynum = int((JD+1.5)%7)
	days = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',\
			5:'Friday',6:'Saturday'}
	return days[daynum]

					# This function returns a day of the week as an output
					# it accepts input from the previous function (i.e. the
					# Julian Day). The 'daynum' is a formula also given in
					# the handout (based on historical facts regarding when
					# the Julian day is considered to begin. I then take that
					# output number and match it in a dictionary I created




# Here I call the functions above. Computing three of the above functions
# for two different inputs (Today's date and the birthdate of the user)

BirthDate = dateinput("Give me your birthdate (ddMmmYYYY): ")
BirthdayDateList = parse(BirthDate)
JDBirthday = JulianDay(BirthdayDateList)
day = DayOfWeek(JDBirthday)


TodayDate = dateinput("Put in today's date (ddMmmYYYY): ")
TodayDateList = parse(TodayDate)
JDToday = JulianDay(TodayDateList)

print ("You were born on a",day)
print ("You've been alive for",int(JDToday-JDBirthday),"days. Congrats!")

				# I wanted to automate the day. I found a function that could
				# return the present time in a chosen format, which I could've
				# possibly placed in a list and run my JulianDay() function
				# on, but I couldn't get it to work. So I chose to do 2 inputs

