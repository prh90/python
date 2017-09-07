from player import Player

pablo = Player("Pablo")

# print(pablo.name)
# print(pablo.lives)
# print(pablo.level)
# print(pablo.score)
pablo.lives -= 1
print(pablo)

pablo.lives -= 1
print(pablo)

pablo.lives -= 1
print(pablo)

pablo.lives -= 1
print(pablo)

# nothing in python is private, can be accessed, only thing we can do is rename it
# If underlined and someone tries to access it, it can cause problems

# getter - gets values
# print(pablo.get_name())
# setter - sets values
# pablo.set_lives(300)
