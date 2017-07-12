# s_string = "bueno"
# s_list = set(s_string)
#
# vowels = set("aeiou")
#
# common = s_list.intersection(vowels)
# print(sorted(common))

# I believe they are both the same  
# *******************************************************8
sampleText = "Python is a very powerful language"

vowels = frozenset("aeiou")

finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)