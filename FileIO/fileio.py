# jabber = open("c:/Users/pablo/Desktop/sample.txt", 'r')
#
# for line in jabber:
#     print(line, end='')
#
# jabber.close()

# with open("c:/Users/pablo/Desktop/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("c:/Users/pablo/Desktop/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("c:/Users/pablo/Desktop/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# # print(lines, end='')
#
# for line in lines:
#     print(line, end= '')

# with open("c:/Users/pablo/Desktop/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# # print(lines, end='')
#
# for line in lines[::-1]:
#     print(line, end= '')

with open("c:/Users/pablo/Desktop/sample.txt", 'r') as jabber:
    lines = jabber.read()
# print(lines, end='')

for line in lines:
    print(line, end= '')

# read returns one whole piece while the others take up memory with multiple storage of each line. Memory will be used up.