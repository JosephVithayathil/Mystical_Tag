"""Apis for film searching."""
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from common_library.status_codes import ApiStatusCodes
from tags_core.models import Movie, Director, Tags


@permission_classes((permissions.IsAuthenticated,))
class SearchAPI(viewsets.ViewSet):
    """API for searching films, directors and tags.
       Input:
        1. k_w : Keyword
       Output:
        1. st: Status
        2. dt: Data{}
            1. movies: List of Movies[{}]
            2. directors: List of Directors[{}]
            2. tags: List of Tags[{}]
    """

    def create(self, request, format=None):
        """POST api."""
        keyword = request.data["k_w"]
        response_data = {}
        if keyword[0] == '#':
            tags = Tags.objects.filter(name__icontains=keyword[1:]).values(
                    'name', 'id')[:15]
            response_data["tags"] = tags
        elif keyword[0] == '&':
            directors = Director.objects.filter(name__icontains=keyword[1:]).values(
                'name', 'id').order_by('popularity', 'name')[:15]
            response_data["directors"] = directors
        else:
            movies = Movie.objects.filter(name__icontains=keyword).values(
                'name', 'id').order_by('popularity', 'imdb_score', 'name')[:15]
            response_data["movies"] = movies
            if len(movies) < 10:
                rest_count = 15 - len(movies)
                directors = Director.objects.filter(name__icontains=keyword).values(
                    'name', 'id').order_by('popularity')[:rest_count]
                response_data["directors"] = directors
                if len(directors) + len(movies) < 15:
                    rest_count = 15 - len(directors) + len(movies)
                    tags = Tags.objects.filter(name__startswith=keyword).values(
                        'name', 'id')[:rest_count]
                    response_data["tags"] = tags
        return Response({"st": ApiStatusCodes.OK, "dt": response_data})
