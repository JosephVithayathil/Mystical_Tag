"""Create edit films."""
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from common_library.status_codes import ApiStatusCodes
from tags_core.models import Movie, Director, Tags


class MovieClass(object):
    """Common class to group all the movie related functions."""

    @staticmethod
    def create_or_edit(film_dict):
        """Common function to create or edit movie.
           Input example:
            film_dict(dict{}):
                {
                    "99popularity": 83.0,
                    "director": "Victor Fleming",
                    "genre": [
                    "Adventure",
                    " Family",
                    " Fantasy",
                    " Musical"
                    ],
                    "imdb_score": 8.3,
                    "name": "The Wizard of Oz"
                }
           Output:
            Movie model object.
        """
        geners = []
        for genre in film_dict["genre"]:
            genre = genre.lstrip().rstrip()
            tag = Tags.objects.get_or_create(name=genre)[0].id
            geners.append(tag)
        director = Director.objects.get_or_create(name=film_dict["director"])[0]
        if film_dict.get("id", None) is None:
            movie = Movie.objects.create(name=film_dict["name"], popularity=film_dict["99popularity"],
                                imdb_score=film_dict["imdb_score"], director=director)
        else:
            movie = Movie.objects.get(id=film_dict["id"])
            movie.name = film_dict["name"]
            movie.popularity = film_dict["99popularity"]
            movie.imdb_score = film_dict["imdb_score"]
            movie.director = director
        movie.tags.add(*geners)
        movie.save()
        return movie


@permission_classes((permissions.IsAdminUser,))
class Create_Edit_Movie_API(viewsets.ViewSet):
    """API for creating and editing movies for Admin users.
       Input:
        1. name : Film Name
        2. genre : List of Genres
        3. director : Director Name
        4. 99popularity : 99popularity
        5. imdb_score : IMDB Rating
        6. id : Send None if creating new movie or ID of the movie if you are editing any movie.
       Output:
        1. st: Status
    """

    def create(self, request, format=None):
        """POST api."""
        request_data = request.data
        film_dict = {}
        film_dict["name"] = request_data["name"]
        film_dict["genre"] = request_data["genre"]
        film_dict["director"] = request_data["director"]
        film_dict["99popularity"] = request_data["99popularity"]
        film_dict["imdb_score"] = request_data["imdb_score"]
        film_dict["id"] = request_data.get("id", None)
        MovieClass.create_or_edit(film_dict)
        return Response({"st": ApiStatusCodes.OK})
