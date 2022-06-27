class Movie:
    def __init__(self,title,year,genre) -> None:
        self._title = title
        self._year = year
        self._genre = genre
    
    def _get_movie(self):
        print(f'Title : {self._title}\nGenre : {self._genre}')

    def print_detail(self):
        self._get_movie()