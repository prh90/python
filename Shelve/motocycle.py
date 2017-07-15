import shelve
# shelve saves into a database
# you can incorrectly save something and it will create a new file if it does not match up to original

with shelve.open("bike") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["colour"] = "red"
    # bike["engine_size"] = 250

    # If error made use this code to locate wrong key and delete it
    # del bike['engin_size']
    for key in bike:
        print(key)

    print('='*40)

    print(bike["engine_size"])
    print(bike["colour"])
