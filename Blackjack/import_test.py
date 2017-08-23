import blackjack
# from blackjack import *

# g = sorted(globals())
# for x in g:
#     print(x)

# print(__name__)
# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play()

# an underscore name is valid but is known as a
# throwaway value

personal_details = ("Pablo", 27, "USA")
name, _, country = personal_details
print(name, country)
print(_)
