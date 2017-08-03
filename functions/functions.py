def python_food():
    width = 80
    text = "Spam and egs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    text = str(text)
    left_margin = (80-len(text)) // 2
    print(" " * left_margin, text)

# call function
# python_food()
# centre_text("Aunt Jemima")
# centre_text("Uncle Roger")
# centre_text(12)

print("first", "second", 3, 4, "spam")