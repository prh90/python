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
print(set_grades)
