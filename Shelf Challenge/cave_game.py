import shelve

locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")

loc = '1'
while True:
    # UPdated to master dictionary so locations and get the exit keys
    availableExits = ", ".join(locations[loc]["exits"].keys())
    # same here
    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        # Also here same principalq
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:   # does it contain a word we know?
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

vocabulary.close()
locations.close()
