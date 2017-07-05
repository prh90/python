#It is recommended to enclose something like t into a ()
# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))
# *************************

# welcome = "Welcome to my nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# print(imelda)
# # print(metallica)
# # print(metallica[0])
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
# *************************
# Cannot reassing a tuple a tuple is like an array but no brackets
# list(array) more flexible
# Makes sense to use a tuple if you do not want the information to be changed
# *************************
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# metallica2[0] = "Master of Puppets"
# print(metallica2)
# ***************************
# imelda = "More Mayhem", "Emilda May", 2011
# imelda = imelda[0], "Imelda May", imelda[2]
# next line is called unpacking the tuple
# title, artist, year = imelda
# print(title)
# print(artist)
# print(year)

# A tuple can have a sub tuple
# imelda = "More Mayhem", "Emilda May", 2011, ((1, "Pulling the ug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# # print(imelda)
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)
# ***********************************************
# Challenge

imelda = "More Mayhem", "Emilda May", 2011, ((1, "Pulling the ug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack: {}, Title: {}".format(track, title))






