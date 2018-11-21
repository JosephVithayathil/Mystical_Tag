"""Views."""
import json
from rest_framework import views
from rest_framework.response import Response
from .apis.create_edit_film import MovieClass


# Create your views here.
class FileUploadView(views.APIView):
    """Api for uploading the imdb json to populate data in database."""

    def post(self, request, filename, format=None):
        """POST function."""
        myfile = request.FILES['file']
        film_list = json.loads(myfile.read())
        for film_dict in film_list:
            MovieClass.create_or_edit(film_dict)
        return Response(status=204)
