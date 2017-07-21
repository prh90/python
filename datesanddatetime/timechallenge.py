import time
import pytz
# import random


all_timezones = ['Africa/Johannesburg', 'America/Chicago', 'Pacific/Auckland', 'Japan', 'Europe/Zurich', 'Europe/Sarajevo', 'Europe/Rome', 'Europe/Moscow', 'Asia/Gaza']


# for x in all_timezones:
#     print("{}: {}".format(all_timezones.index(x) + 1, x))
tim1 = 'Africa/Johannesburg'
tim2 = 'America/Chicago'
tim3 = 'Pacific/Auckland'
tim4 = 'Japan'
tim5 = 'Europe/Zurich'
tim6 = 'Europe/Sarajevo'
tim7 = 'Europe/Rome'
tim8 = 'Europe/Moscow'
tim9 = 'Asia/Gaza'
l_exit = 'Exit'

l_list = [tim1, tim2, tim3, tim4, tim5, tim6, tim7, tim8, tim9, l_exit]

for x in l_list:
    if x == l_exit:
        print("0: Exit")
    else:
        print("{}: {}".format(l_list.index(x) + 1, x))

print()
int1 = input("Select the timezone you would like to see: ")
print(int1)




