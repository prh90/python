import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)    # creating absolute path
            yield os.path.join(absolute_path, file)  # us it in yielded values


error_list = []

for f in find_music('music', 'emp3'):
    try:
        id3er = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3er.get_value("performer"),
            id3er.get_value("album"),
            id3er.get_value("track"),
            id3er.get_value("title")
        ))
    except:
        error_list.append(f)

print("*"*50)
for error in error_list:
    print(error)
