my_set = {1, 3, 5}
# list within dicitonary
my_dict = {'name': 'Jose', 'age': 90, 'grades': [13, 45, 66, 90]}
another_dict = {1: 15, 2: 75, 3: 150}

lottery_player = {
    'name': 'Rolf',  # tuple within dictionary
    'numbers': (13, 45, 66, 23, 22)
}
# List of dictionaries
# universities = {
#     {
#         'name': 'Oxford',
#         'location': 'UK'
#     },
#     {
#         'name': 'MIT',
#         'location': 'US'
#     }
# }

# sum(lottery_player['numbers'])  # Can access a key

# lottery_player['name'] = 'John'  # Reassign

##
print(sum(my_dict['grades']))
