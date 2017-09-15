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

def getint():
    while True:
        try:
            number = int(input("Please enter a number: "))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
