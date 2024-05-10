
# Importar los módulos necesarios para la ejecución del programa.
from genre import GENRE
from datetime import date

class Song():
    """Constructor of the class.

        The constructor of the class Song is used to create a new song.

        Syntax
        ------
          song = Song(id, name, artist, duration, release_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the song.
          name : str
            The name of the song.
          artist : str
            The artist of the song.
          duration : int
            The duration of the song in seconds.
          release_date : date
            The release date of the song.
          genres : list
            The genres of the song.

        Returns
        -------
          The new song.

        Example
        -------
          song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])
        """
    #Realizar la implementación de la clase Song.
    def __init__ (self, id, name, artist, duration, release_date, genres):
        self.id = id
        self.name = name
        self.artist = artist
        self.duration = duration
        self.release_date = release_date
        self.genres = genres

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration

    def get_release_date(self):
        return self.release_date

    def get_genres(self):
        return self.genres

    def set_id(self, id):
        if isinstance(id, int):
            self.id = id
        else:
            raise TypeError("ID must be an integer.")

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string.")

    def set_artist(self, artist):
        if isinstance(artist, str):
            self.artist = artist
        else:
            raise TypeError("Artist must be a string.")

    def set_duration(self, duration):
        if isinstance(duration, int) and duration > 10:
            self.duration = duration
        else:
            raise ValueError("Duration must be an integer greater than 10.")

    def set_release_date(self, release_date):
        if isinstance(release_date, date):
            if release_date <= date.today():
                self.release_date = release_date
            else:
                raise ValueError("Release date cannot be a future date.")
        else:
            raise TypeError("Release date must be a valid date object.")


    def set_genres(self, genres):
        if isinstance(genres, GENRE):
            self.genres = genres
        else:
            raise TypeError("Genres must be a list.")
        
    def add_genre(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

    def __str__(self):
      return f"{self.artist} tocando {self.name} durante {self.duration} segundos."
    
    def __eq__(self, other):
      return self.id == other.id

def main():
    """Function main of the module.

    The function main of this module is used to test the Class Song.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Song.")
    print("=================================================================.")
    song = Song(1, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if song.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_name() == "calorro":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_artist() == "estopa":
        print("Test PASS. The parameter artist has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_duration() == 189:
        print("Test PASS. The parameter duration has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_release_date() == date.today():
        print("Test PASS. The parameter release_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if song.get_genres() == [GENRE.POP]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    song2 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])

    if str(song2) == "estopa tocando calorro durante 189 segundos.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(song2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(song2))


    print("=================================================================.")
    print("Test Case 3: song add_genre")
    print("=================================================================.")
    song2.add_genre(GENRE.ROCK)
    genres = song2.get_genres()
    if genres == [GENRE.POP, GENRE.ROCK]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    song3 = Song(2, "calorro", "estopa", 189, date.today(), [GENRE.POP])
    if song2 == song3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")
    


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()