locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside of a building, a well house for a small stream",
             4: "You are on a valley beside a stream",
             5: "You are in the forest"
             }
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"N": 2, "S": 1, "Q": 0}
         }

vocabulary = {"QUIT":  "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST":  "E",
              "WEST":  "W"}

# print(locations[0].split())
# print(locations[3].split())
# print(' '.join(locations[0].split()))



loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available Exits are " + availableExits + " ").upper()
    print()
    # Parse user input using vocab dictionary
    if len(direction) > 1:
        words = direction.split()
        for word in words :
            for word in vocabulary:
                direction = vocabulary[word]
                break
        # for word in vocabulary: # does it contain word we know
        #     if word in direction:
        #         direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")




# while True:
#     mylist = ["a", "b", "c", "d"]
# letters = ["abcdefghijklmnopqrstuvwxyz"]
# numbers = "123456789"
#
# newString = ''
# for c in mylist:
#     newString = " mississippi ".join(numbers)
#
# print(newString)



################################################33
# Original code before the challenge


# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside of a building, a well house for a small stream",
#              4: "You are on a valley beside a stream",
#              5: "You are in the forest"
#              }
# exits = [{"Q": 0},
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          {"N": 5, "Q": 0},
#          {"W": 1, "Q": 0},
#          {"N": 1, "W": 2, "Q": 0},
#          {"N": 2, "S": 1, "Q": 0}
#          ]
# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#     # availableExits = ""
#     # for direction in exits[loc].keys():
#     #     availableExits += direction + ", "
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available Exits are " + availableExits + " ").upper()
#     print()
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")
