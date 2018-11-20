"""Create edit films."""
from tags_core.models import Tags, Director, Movie

class MovieClass(object):

    @staticmethod
    def create(film_dict):
        print(film_dict)
        geners = []
        for genre in film_dict["genre"]:
            genre = genre.lstrip().rstrip()
            tag = Tags.objects.get_or_create(name=genre)[0].id
            geners.append(tag)
        director = Director.objects.get_or_create(name=film_dict["director"])[0]
        print(director)
        movie = Movie.objects.create(name=film_dict["name"], popularity=film_dict["99popularity"],
                             imdb_score=film_dict["imdb_score"], director=director)
        movie.tags.add(*geners)
        movie.save()
