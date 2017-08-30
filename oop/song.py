class Song:
    """ Class to represent a song

    Attributes:
        title (str): The title of the song
        artist(Artist): An artist object representing the songs creator
        duration(int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an Album, using its tracklist

    Attributes:
        Album_name (str): The name of the album
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
            song (Song): A song to add.
            position (optional[int]): If specified, the song will be added to that position in the track list - inserting it between other songs if necessary.
            Otherwise, song will be added at the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)
