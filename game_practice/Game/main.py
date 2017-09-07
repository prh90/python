from player import Player

pablo = Player("Pablo")

from enemy import Enemy

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

random_monster.take_damage(12)
print(random_monster)

# nothing in python is private, can be accessed, only thing we can do is rename it
# If underlined and someone tries to access it, it can cause problems

# getter - gets values
# print(pablo.get_name())
# setter - sets values
# pablo.set_lives(300)
