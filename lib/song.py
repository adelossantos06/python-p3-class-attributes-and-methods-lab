class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, artist, genre, artist_count=None, genre_count=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre_count)
        self.add_to_artist_count(self.artist_count)

    def add_to_genre_count(self, genre_count):
        if self.genre_count.get(self.genre):
            self.genre_count[self.genre] += 1
        else:
            self.genre_count[self.genre] = 1

    def add_to_artist_count(self, artist):
        if self.artist_count.get(self.artist):
            self.artist_count[self.artist] += 1
        else:
            self.artist_count[self.artist] = 1

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    
    