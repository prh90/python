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
print(player_one.name == player_two.name)
print(player_one.numbers == player_two.numbers)
