import shelve

# A shelve is a read/write by nature
with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus, fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour , yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])
# If code is outside the with statement you receive an error because the 'with' closes the loop as soon as block ends
#############################################
# This is the manual way to open and close

# fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus, fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour , yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"
#
# print(fruit["lemon"])
# print(fruit["grape"])
# this is to explicitly tell it to close
# fruit.close()