# for i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#
# available_exists = ["east", "north east", "south"]
# chosen_exit = ""
#
# while chosen_exit not in available_exists:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
# else:
#     print("arent you glad you got out of there!")
#

# Guessing game from ealier
# import random
#
# highest = 10
# answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}: ".format(highest))
#
# guess = int(input())
#
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well Done, youve guessed it")
#     else:
#         print("Sorry you have not guessed it correctly")
# else:
#     print("Well Done, youve guessed it on the first try")
#
#
# Challenge-----------------------
# import random
#
# highest = 10
# answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}: ".format(highest))
#
# guess = int(input())
#
# while guess != answer:
#     if guess == 0:
#         print("You quit, it was {}".format(answer))
#         break
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
# else:
#     print("Well Done, youve guessed {} correctly".format(answer))
#
# Tim answer

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))

guess = 0 # initialize to any number outside of the valid range

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("You quit, it was {}".format(answer))
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well Done, youve guessed {} correctly".format(answer))





#
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well Done, youve guessed it")
#     else:
#         print("Sorry you have not guessed it correctly")
# else:
#     print("Well Done, youve guessed it on the first try")


