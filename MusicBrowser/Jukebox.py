import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect('music.sqlite')


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        #  tkinter.Listbox.__init__(self, window, **kwargs) # python2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # python 3 code
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # it calls the super on scrollbox
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self, link_value=None):
        if link_value:
            sql = self.sql_select + " WHERE " + "artist" + "=?" + self.sql_sort
            print(sql)  # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)  #  TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        #  clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

    def get_albums(self, event):
        lb = event.widget
        index = lb.curselection()[0]
        # print(index)
        artist_name = lb.get(index),
        # print(artist_name)

        # get the artist ID from the database row
        artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()[0]
        albumList.requery(artist_id)

        # artist_id = conn.execute("SELECT artists._id FROM
        # artists WHERE artists.name=?", artist_name).fetchone()
        # alist = []
        # for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ?
        # ORDER BY albums.name", artist_id):
        #     alist.append(row[0])
        # albumLV.set(tuple(alist))
        # songLV.set(("Choose an album",))


def get_songs(event):
    lb = event.widget
    print(lb.curselection()[0])
    index = int(lb.curselection()[0])
    print(index)
    album_name = lb.get(index),
    print(album_name)

    # get the artist ID from the database
    album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
    alist = []
    for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album = ? ORDER BY songs.track", album_id):
        alist.append(x[0])
    songLV.set(tuple(alist))


mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browswer")
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # spacer column on the right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ===== labels =====
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ===== Artists Listbox =====
# artistLV = tkinter.Variable(mainWindow)
# artistLV.set(("Artist",))
# artistList = Scrollbox(mainWindow, listvariable=artistLV)
# Added the above code to test it out
# artistList = Scrollbox(mainWindow)
artistList = DataListBox(mainWindow, conn, "artists", "name")
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

artistList.requery()
artistList.bind('<<ListboxSelect>>', get_albums)

# ===== Albums Listbox =====
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
albumList = DataListBox(mainWindow, conn,  "albums", "name", sort_order=("name",))
albumList.requery()
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

albumList.bind('<<ListboxSelect>>', get_songs)


# ===== Songs Listbox =====
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = DataListBox(mainWindow, conn, "songs", "title", sort_order=("track", "title"))
songList.requery()
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')


# ===== Mainloop =====
# testList = range(0, 100)
# albumLV.set(tuple(testList))
# artistLV.set(tuple(testList))
# albumLV.set((1, 2, 3, 4, 5))
mainWindow.mainloop()
print("Closing database connection")
conn.close()
