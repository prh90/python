import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-5].split(' - ')
            print(song_details)
        print("*"*50)
    # print(directories)
    # print(files)
    # input()
    # for f in files:
    #     print("\t{}".format(f))

# os.walk is a generator that it doesnt try to read
# every single file at once. its only yielding the
# information from single directory at a time
