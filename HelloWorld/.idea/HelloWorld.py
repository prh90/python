# The questions could be refactoed
# print("Please Enter your name: ")
# name = input()
# print("Please enter your age: ")
# age = int(input())
#
# if (17 < age < 31):
#     print("Welcome to the Holiday {}".format(name))
# else:
#     print("I am sorry you cannot participate in the holiday {}".format(name))

#
name = input("Please enter your name: ")
age = int(input("What is your name, {0}?".format(name)))
if (17 < age < 31):
    print("Welcome to the Holiday {}".format(name))
else:
    print("I am sorry you cannot participate in the holiday {}".format(name))


# if (age >= 16) and (age <= 65):
#     print("have a good day at work")
# else:
#     print("Get some rest!")

# shorter version to the code above
# if (16 <= age <= 65):
#     print("have a good day at work")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
# Using the input for feedback
# x = input("Please enter some text: ")
#
# if x:
#     print("You've entered '{}' ".format(x))
# else:
#     print("You didnt enter any text!")


# age = 24
# print("My age is " + str(age) + " years")
# print("My age is {0} years".format(age))
#
# for i in range(1, 12):
#     print("No %2d squared is %4d and a cubed is $%4d" %(i, i ** 2, i ** 3))
#
# print("Pi is approx {0:12.50}".format(22 / 7))
#
# for i in range(1, 12):
#     print("No {0:2} squared is {1:<4} and a cubed is {2:<4}".format(i, i ** 2, i ** 3))
#
# for i in range(1,12):
#     print("No {} squared is {} and a cubed is {}".format(i, i ** 2, i ** 4))
#
# Work in inout and conditional

# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}?".format(name)))
# print(age)
#
# if age >= 18:
#     print("Youre old enough to vote")
# else:
#     print("Please comeback in {0} years".format(18 - age))
#
# Conditional that can be refactored to make more sense
# print("Please guess a number between 1 and 10")
# guess = int(input())
#
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done youve guessed it")
#     else:
#         print("Sorry you have not guessed it")
# elif guess > 5:
#     print("please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done youve guessed it")
#     else:
#         print("Sorry you have not guessed it")
# else:
#     print("You got it first time")

