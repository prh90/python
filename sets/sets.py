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
# even = set(range(0, 40, 2))
# print(even)
#
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(squares)

# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8) #no error, does nothing
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not part of the set")
# if 8 in squares:
#     squares.remove(8)
# # Safe way to check if its inside if it is then proceed with operation

# even = set(range(0, 40, 2))
# # print(even)
#
# square_tuple = (4, 6, 16)
# squares = set(square_tuple)
# # print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")

even = frozenset(range(0, 100, 2))

print(even)
even.add(3)


