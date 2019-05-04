Timer server



I run the program using "Server.py"


Now this just leaves a blank space open (similar to if you type "echo" in
the command line)

I then go to a different terminal and type "nc 127.0.0.1 55555"

which is netcat, a utility for checking TCP (or UDP I suppose) connections

So We check the internal ip address via port 55555

After typing this command in, in the ORIGINAL window I ran "Server.py"
the following shows up:


Connection successful
Current time: 03:25 PM



potential snag:
I have to wait a few minutes to do this again. I can't get the connection to
close right away :/ If I had more time I would've figured out just how to 
correct this

I get this if I try and run it again:

Traceback (most recent call last):
  File "./Server.py", line 21, in <module>
    s.bind((host,port))
OSError: [Errno 98] Address already in use




fin
