#!/usr/bin/env python3.9

import time
start_time = time.localtime()
print(f"Time started at {time.strftime('%X', start_time)}")

#comment wait for user to stop time
input ("press enter to stop it")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print (f"timer stopped at {time.strftime('%X', stop_time)}")
print (f"Total time: {difference} seconds")

