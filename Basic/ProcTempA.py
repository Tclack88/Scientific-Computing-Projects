#!/usr/bin/python3

#PURPOSE: display processor temperature every second (compare to 2nd part)

import subprocess
import time
# subprocess contains many commands that are useful, in particular
# subprocess.call() which allows me to run a Linux command

while True:        #I'm using this to invoke the infinite loop

# subprocess.check_output lets me use a linux command that I want
# namely to read the "file" temp in /sys/class/thermal/thermal_zone0
# This output would normally go to a file on the system known as the
# standard output and it would be shown as:  b'OUTPUT_HERE\n'
# adding "universal_newlines=True" interprets the /n as a new line
# Using standard python variable usage, I set all that as the variable "temp"


	temp = subprocess.check_output\
	(['cat', '/sys/class/thermal/thermal_zone0/temp'],universal_newlines=True)

# Next, This output file is just a string, so I make it a float with "float(temp)
# all the meanwhile changing this to the new variable temp, destroying the
# old one. Dividing by 1000.0 converts from millicelcius to Celcius

	temp = float(temp)/1000.0

# Then I just have it print all this info then wait a second and it repeats
# the process over again, because of the "While True" loop

	print ("The current processor temperature is: ", temp, "degrees Celcius")

	time.sleep(1)
