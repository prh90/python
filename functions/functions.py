def python_food():
    width = 80
    text = "Spam and egs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    left_margin = (80-len(text)) // 2
    print(" " * left_margin, text)

# call function
# python_food()
centre_text("Aunt Jemima")