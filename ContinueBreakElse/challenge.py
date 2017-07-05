# ipAddress = input("Please enter your IP address: ")
#
# segment = 1
# segment_length = 0
# character = ""
#
# for character in ipAddress:
#     if character == '.':
#         print("segment {} contains {} characters".format(segment, segment_length))
#         segment += 1
#         segment_length = 0
#     else:
#         segment_length += 1
# # Unless the final character in a string was a dot then we havent printed the last segment
# if character != ".":
#     print("segment {} contains {} characters".format(segment, segment_length))

ipAddress = input("Please enter your IP address: ")

if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
# character = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# # Unless the final character in a string was a dot then we havent printed the last segment
# if character != ".":
#     print("segment {} contains {} characters".format(segment, segment_length))
