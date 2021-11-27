from datetime import datetime
import pytz
import time

milliseconds = int(round(time.time() * 1000))

print("Current time in Milli seconds is : ", milliseconds)
tz_IN = pytz.timezone('UTC') 
now = datetime.now(tz_IN)

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)