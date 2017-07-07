# farm_animals = {"sheep", "cow", "hen"}
#
# for animal in farm_animals:
#     print(animal)
#
# print("*"* 50)
# wild_animals = set({"lion", "tiger", "panther", "elephant","hare"})
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# Sets aer really complicated
#
# even = set(range(0, 40, 2))
# print(sorted(even))
#
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minues even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print("*"* 50)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
#
#
even = set(range(0, 40, 2))
print(even)

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(squares)

# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))







