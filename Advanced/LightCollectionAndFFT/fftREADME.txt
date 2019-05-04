Acquire and Store Data

With ADC and solar cell plugged in to the raspberry pi, I run the program using
 "LightDataCollect.py" and it returns data from the collection labeleled as "LightData.txt"

If you look at this file set, you'll notice there are two text files:

"LightData.txt" and "LightExampleData.txt"
If you run the program it will return and overwrite the preexisting 
"LightData.txt" but the eps file for this problem (LightData.eps) is based on the 
data from "LightExampleData.txt", so I wanted to preserve that data. Feel to run
the program and test it, I won't lose my "example data"


Anyway, when I run it I get the following output (plus a new data file):


Press <Enter> to start 1.0 s data acquisition...

Time elapsed: 1.043963883.

creating data text file (LightData.txt) for this run.... 

LightData.txt created. Press <Enter> to exit...

.
.
.
.
.
.
.
.
.
.
.
.


Fourier Analysis


A. I downloaded a strobe app on my phone which strobes at about 10 flashes/sec

I ran my LightDataCollect.py program with this strobe focused on the solar cell and
collected and stored the data as "fftdata.txt"




B. The "fft.py" program is the one that reads that data and generates a plot
It's called with an arguement!!!
Even though it's less convenient, I thought it was a better choice, because
it can be applied to other data files.

So I run it with "fft.py fftdata.txt" and it returns two plots:
a reconstruction of the original data (which I have saved here anyway as
fftdata.eps) as well as the power spectrum. It also yields the following to
standard output:



Peak Frequency: -10.3125

Showing plot and power spectrum. Press <Enter> to exit...


I liked getting the exact frequency displayed so it didn't just have to be
eyeballed




C. The eps is saved here as fftdata.eps

(You may notice that if you run the program as described in part B on the data
that the Power Spectrum will be squished more to the left compared to the
figure saved here. That is because I have part b setup to work on general input
so the entire power spectrum range is the "x-axis". In thie figure saved, I 
restricted the domain for visibility. However if new data was ran with a much
higher frequency source, such as the fluorescent bulbs, my original domain size
set for my phone flasher wouldn't show up on the plot)
fin
