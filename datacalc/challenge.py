import time

types = ['time', 'monotonic', 'perf_counter', 'process_time']


for x in types:
    print(time.get_clock_info(x))
# Wrote code to display all of the times for better understanding