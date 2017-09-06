from player import Player

pablo = Player("Pablo")

print(pablo.name)
print(pablo.lives)
print(pablo.level)
print(pablo.score)
pablo.lives -= 1
print(pablo.lives)

dad = Player("Dad")
print(dad.name)

mom = Player("mom")
print(mom.name)