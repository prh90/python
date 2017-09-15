# def mult():
#     num1 = input("Enter the first number: ")
#     num2 = input("Now enter the second number: ")
#
#     print("{} / {} = {}".format(num1, num2, (int(num1)//int(num2))))
#
#
# try:
#     mult()
# except ZeroDivisionError:
#     print("Cant divide by zero son")
###########################################################################
import sys

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        # When handling multiple errors, make sure you get them in the right order because it can loop
        # More specific exceptions go first
        except EOFError:
            sys.exit(1)
        except:  # ValueError # If empty it takes all errors known as wildcard except
            print("Invalid number entered, please try again")
        finally:
            print("The Finally clause always executes")


first_number = getint("Please enter first number: ")
second_number = getint("Please enter second number: ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Cant divide by zero son")
    sys.exit(2)
else:
    print("Division performed successfully")