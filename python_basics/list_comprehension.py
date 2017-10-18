my_list = [0, 1, 3, 4]

an_equal_list = [x for x in range(5)]  # [0, 1, 3, 4]
# print(an_equal_list)
multiply_list = [x * 3 for x in range(5)]
# print(multiply_list)
# print(11 % 3)  # = 2 why? 9 fits into 11 and remainder 2

print([n for n in range(10) if n % 2 == 0])
