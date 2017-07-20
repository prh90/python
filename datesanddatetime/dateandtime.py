import time

print("The Epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with and offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight saving time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
