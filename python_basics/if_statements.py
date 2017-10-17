# should_continue = True
#
# if should_continue == True:
#     print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}!".format(person))

# Challenge


def who_do_you_know():
    # Ask the user for a list of the people they know
    string = str(input("Please enter a list of people you know: "))
    # Split the string into a list
    p_list = string.split(",")
    # Return that list
    return ask_user(p_list)


def ask_user(p_list):
    # Ask user for a name
    name = input("Who are you looking for?: ")
    # See their name is in the list of people they know
    if name in p_list:
        # Print out that they know the person
        print("You know {}".format(name))
    else:
        print("You dont know {}".format(name))


who_do_you_know()
