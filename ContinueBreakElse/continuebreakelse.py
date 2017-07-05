# shopping_list = ["Milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     # This embedded code if matched will skip spam
#     # continue will skip matched item and keep going through array
#     if item == "spam":
#         continue
#     print("Buy "+ item)
#
# meal = ["egg", "bacon", "spam", "sausages"]
# nasty_food_item = ''
#
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
#
# else:
#     print("i'll have a plate of that please!")
# if nasty_food_item:
#     print("Can't I have anything without spam in it?")

# Augmented Assignment

# number = "9, 223, 372, 036, 854, 775, 807"
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))
