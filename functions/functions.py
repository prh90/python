def python_food():
    width = 80
    text = "Spam and egs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80-len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)

# call function
# python_food()
centre_text("Aunt Jemima")
centre_text("Uncle Roger")
centre_text(12)
centre_text("first", "second21", 3, 4, "spam", sep=":")
