import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["Tin of soup"]
pasta = ["Pasta", "Cheese"]

with shelve.open('recipes') as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrabled eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
