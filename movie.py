import logging
from pathlib import Path
import json

DATA_FILE = Path.cwd().resolve() / "data" / "movies.json"


def get_movies():

    with open(DATA_FILE, "r") as f : 
        movies_title = json.load(f)
        
    return [Movie(movie_title) for movie_title in movies_title]

    
class Movie:
    
    def __init__(self, title) -> None:
        self.title = title.title()
        
        
    def __str__(self) -> str:
        return self.title
    
    
    def add_to_movies(self):
        movies = self._get_movies()
        movie = self.title
        if movie in movies:
            logging.warning(f"le film {movie} est déjà enregistré")
            return False
        else : 
            movies.append(movie)
            self._write_movies(movies)
            return True
    
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies,f, indent=4)
            
            
    def remove_from_movies(self):
        movies = self._get_movies()
        movie = self.title
        if movie in movies: 
            movies.remove(movie)
            self._write_movies(movies)
            
        
    
if __name__ == "__main__":
    film = Movie("jar")