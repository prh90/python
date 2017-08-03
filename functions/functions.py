def python_food():
    width = 80
    text = "Spam and egs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80-len(text)) // 2
    return " " * left_margin + text

# with open("centered", mode="w") as centred_file:

# call function
print(centre_text("Aunt Jemima"))
print(centre_text("Uncle Roger"))
print(centre_text(12))
print(centre_text("first", "second21", 3, 4, "spam", sep=":"))
