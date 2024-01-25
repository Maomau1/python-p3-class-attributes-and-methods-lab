class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}

    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre =  genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre) 
        # if genre not in cls.genres else None

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        pass

    @classmethod
    def add_to_artist_count(cls):
        pass


