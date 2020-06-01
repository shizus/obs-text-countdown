from datetime import datetime, timedelta
import time


def time_delta_to_string(time_delta):
	str_time_delta = str(time_delta)
	hours, minutes, seconds = str_time_delta.split(':')
	return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(float(seconds)))


now = datetime.now()

time_string = '00:27:10'

hours, mins, seconds = time_string.split(':')

delta = timedelta(hours=int(hours), minutes=int(mins), seconds=int(seconds))
end = now + delta
activity = "Working"
while end > now:
	now = datetime.now()
	remaining_time = end - now
	f = open("countdown.txt", "w")
	f.write("{activity}! {time}".format(
		activity=activity,
		time=time_delta_to_string(remaining_time)))
	f.close()
	time.sleep(1)
