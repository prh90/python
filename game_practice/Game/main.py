from player import Player

pablo = Player("Pablo")

from enemy import Enemy, Troll, Vampire, VampireKing

# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(12)
# print(random_monster)
######################################################################

# Testing inheritance out with Troll class
ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))
ugly_troll.grunt()
print("*"*50)

another_troll = Troll("Trollski")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(15)
another_troll.grunt()
print("*"*50)

######################################################################

# Vampire class created as a challenge
vamp = Vampire("Vlad")
print("A vampire - {}".format(vamp))
vamp.take_damage(10)
# print("Hit Points left: {}".format(vamp.hit_points))
print("*"*50)

another_vamp = Vampire("Dracula")
print("Another Vampire -{}".format(another_vamp))

# while another_vamp._alive:
#     another_vamp.take_damage(1)
#     print(another_vamp)
######################################################################
pab = VampireKing("Pabs")
print(pab)
pab.take_damage(9)
print(pab)

######################################################################


# nothing in python is private, can be accessed, only thing we can do is rename it
# If underlined and someone tries to access it, it can cause problems
# getter - gets values
# print(pablo.get_name())
# setter - sets values
# pablo.set_lives(300)
