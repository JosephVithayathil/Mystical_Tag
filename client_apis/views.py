"""Views."""
import json
from rest_framework import views
from rest_framework.response import Response
from .apis.create_edit_film import MovieClass


# Create your views here.
class FileUploadView(views.APIView):

    def post(self, request, filename, format=None):
        myfile = request.FILES['file']
        film_list = json.loads(myfile.read())
        for film_dict in film_list:
            MovieClass.create(film_dict)
            # break
        return Response(status=204)