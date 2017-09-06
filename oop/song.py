class Song:
    """ Class to represent a song

    Attributes:
        title (str): The title of the song
        artist(Artist): An artist object representing the songs creator
        duration(int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.name = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an Album, using its tracklist

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The Artist responsible for the album.
            If not sepcified the artist will default to an artist with the name "Various Artists"
        tracks (List[Song]): A list of the songs on the album

    Methods:
        add_Song: Used to add a new song to the album's track list
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): Title of the song to add.
            position (optional[int]): If specified, the song will be added to that position
             in the track list - inserting it between other songs if necessary.
            Otherwise, song will be added at the end of the list
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Store artist details

    Attributes:
        name (str): The name of the artist
        albums (List{Album}): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not and exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again
                (although this is yet to be implemented)
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """ Add a new song to the collection of albums

        This method will add the new song to an album in the collection.
        A new album will be created in the collection if it doesn't already exist.

        Args:
            name (str): The name of the album
            year (int): The year the album was produced
            title (str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


# def load_data():
#     new_artist = None
#     new_album = None
#     artist_list = []
#
#     with open("albums.txt", "r") as albums:
#         for line in albums:
#             # data row should consist of (artist, album, year, song)
#             artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
#             year_field = int(year_field)
#             print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
#
#             if new_artist is None:
#                 new_artist = Artist(artist_field)
#             elif new_artist.name != artist_field:
#                 # we've just read details for a new artist
#                 # store the current album in the current artist
#                 # collection then create a new artist object
#                 new_artist.add_album(new_album)
#                 artist_list.append(new_artist)
#                 new_artist = Artist(artist_field)
#                 new_album = None
#
#             if new_album is None:
#                 new_album = Album(album_field, year_field, new_artist)
#             elif new_album.name != album_field:
#                 # We've just read a new album for the current artist
#                 # store current album in the artist's collection then create a new album object
#                 new_artist.add_album(new_album)
#                 new_album = Album(album_field, year_field, new_artist)
#
#             # create a new song object and add it to the current album's collection
#             new_song = Song(song_field, new_artist)
#             new_album.add_song(new_song)
#
#         # After reading the last line of the text file, we will have an artist
#         # and album that haven't been store - process them now
#         if new_artist is not None:
#             if new_album is not None:
#                 new_artist.add_album(new_album)
#             artist_list.append(new_artist)
#
#     return artist_list

def find_object(field, object_list):
    """ Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(album_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list

# def create_checkfile(artist_list):
#     """Create a check file from the object data for comparison with the original file"""
#     with open("checkfile.txt", 'w') as checkfile:
#         for new_artist in artist_list:
#             for new_album in new_artist.albums:
#                 for new_song in new_album.tracks:
#                     print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)


def create_checkfile(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song), file=checkfile)

if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)
