import time
import pytz
# import random

# # Prints the whole list of acceptable timezones
# for x in pytz.all_timezones:
#     print(x)
all_timezones = ['Africa/Johannesburg', 'America/Chicago', 'Pacific/Auckland', 'Japan', 'Europe/Zurich', 'Europe/Sarajevo', 'Europe/Rome', 'Europe/Moscow', 'Asia/Gaza']

for x in all_timezones:
    print("{}: {}".format(all_timezones.index(x) + 1, x))
print("0: Exit")

choice = input("Choose one to see the time: ")

if choice == 0:
    
else:
    print("OK")