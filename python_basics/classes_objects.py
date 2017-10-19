lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


# Each new instance is distinct and not the same even if you compare using ==
player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("Adam")
# print(player_one.name == player_two.name)
# print(player_one.numbers == player_two.numbers)

##


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return (sum(self.marks)/len(self.marks))

    # you can take self oyt by doing this adding cls classmethod
    # @classmethod
    # or you can pass in
    @staticmethod  # and you dont pass anything in as an arguemnt
    def go_to_school():
        # print("I'm going to {}".format(self.school))
        print("I'm going to school")
        # print("I'm a {}".format(cls))


anna = Student("Anna", "MIT")
anna.go_to_school()
# If we ran taking self out of the go to school method
# It will fail becuase you technically pass an argument
# in the name of the object itself, so you are passinbg in anna
Student.go_to_school()  # can also call it by class itself
# anna.marks.append(56)
# anna.marks.append(71)
# anna.marks.append(63)
# print(anna.marks)
# print(anna.average())
