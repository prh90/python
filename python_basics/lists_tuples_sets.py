# Most flexible can modify
list_grades = [77, 80, 90]
# tuples are inmutable - cannot increase size - no modification
tuple_grades = (77, 80, 90)
# set is unique and unordered
set_grades = {77, 80, 90}

# print(sum(list_grades) / len(list_grades))

list_grades.append(100)
# print(list_grades)

# To add to the tuple
tuple_grades = tuple_grades + (100,)
# print(tuple_grades)

# to add to a set
set_grades.add(60)
# print(set_grades)


################################## Set Operations

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

# print(set_one.intersection(set_two))
# print(set_one.union(set_two))
print(set_two.difference(set_one))
