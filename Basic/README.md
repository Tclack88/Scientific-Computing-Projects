# Early projects (Basic)
A collection of some of my early scientific computation projects.
Each code has explanation of insights gained during the writing process in the code comments themselves, however I will provide a brief description for each here


## fibonnaci.py
User provides an integer n as input. The program prints the first n Fibonacci numbers up to 80 (merely because numbers beyond this size are impeded by the default terminal size)

![fibonacci example](fibonacci.png)

## InfoAssist.py
This program takes a csv file, excel spreadsheet, etc. with specific columnar information and creates a dictionary with that information. It then takes input from the user to display requested information. It's much like a limited form of SQL

## InputParsing.py
This is basic string parsing

## JulianDayCalc.py
This program takes your birthday and today's date (or any other arbitrary day you wish) then determines the day of the week you were born on and the number of days you've been alive for. It does this by tracking the Julian date.

## PrimeFactor.py
This program prime factorizes a number given via input

## ProcTempA.py and ProcTempB.py
ProcTempA.py displays the processor temperature every second (ProcTempB.py just prints something really fast in order to demonstrate that such a process will raise the temperature). This is described more thoroughly in "ProcTempREADME.txt"

## SinCosPlot.py
My first work with matplotlib plotting sine and cosine over 2.5 cycles. This is included here more for historical purposes

## SineSeriesApprox.py
The purpose of this was to analyze and compare the differences between the python math module's built in sine function and sine as defined by the Taylor series (approximation, The number of terms used in the series is chosen by the user at input and both the absolute difference and ratio are returned

## windplot.py and wind.dat
The purpose of this program is to plot x,y data with error bars. The original intention was to find wind speed as a function of time of day out of curiosity. The program takes an argument specifying the file, so it can be used for any similar file, it also checks file permissions (i.e. whether it exists, and whether or not the person trying to use it has access permission). "wind.dat" is included as an example (the original data gathered actually)
