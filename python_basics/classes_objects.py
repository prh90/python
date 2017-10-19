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


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
anna.marks.append(63)
print(anna.marks)
print(anna.average())
