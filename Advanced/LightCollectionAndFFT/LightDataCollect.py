#!/usr/bin/env python3

# PURPOSE: used to collect data for fft.py, collects light from solar panel fed into
# analog-to-digital-converter component Adafruit ADS1x15 

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import os
from Adafruit import ADS1x15

ACQTIME = 1.0  # seconds of data acquisition

SPS = 920
VRANGE = 4096
nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS
					# Establish samples/sec and voltage range (mV), use those
					# to determing number of samples and a sample interval
indata = np.zeros(nsamples,'float')

					# establish an empty array to put our data values in


adc = ADS1x15()
adc.startContinuousDifferentialConversion(2, 3, pga=VRANGE, sps=SPS)

					# a lot going on under the hood. Calling ADS1x15() imports
					# many libraries necessary for the hardware to function
					# The ADC is then initiated to start collecting

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter()
   indata[i] = 0.001*adc.getLastConversionResults()
   while (time.perf_counter() - st) <= sinterval:
      time.sleep(1.0e-7)

					# Presumably 'getLastConversionResults() outputs a voltage
					# so we multiply by .001 to convert to mV and add that to
					# the ith array position. While the difference of the
					# current time from the time this for loop began is less
					# than our interval, the loop will sleep 

t = time.perf_counter() - t0
adc.stopContinuousConversion()
xpoints = np.arange(0, ACQTIME, sinterval)
print('Time elapsed: %.9f.' % t)

					# stop the conversion, set the x-axis values, print the
					# total time elapsed (just because)

f1, ax1 = plt.subplots()
ax1.plot(xpoints, indata)
f1.show()

					# standard plotting commands


print ("\ncreating data text file (p4data.txt) for this run.... ")

os.system("rm lightdata.txt -f")

for i in indata:
	addition = "echo "+str(i)+" >> lightdata.txt"
	os.system(addition)
	
					# remove p4data.txt if it already exists, this way when
					# the for loop appends, it won't append to data from
					# previous runs				

input("\nlightdata.txt created. Press <Enter> to exit...\n")
