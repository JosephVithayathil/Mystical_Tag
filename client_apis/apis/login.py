"""Apis for player signup."""
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from common_library.status_codes import ApiStatusCodes


@permission_classes((permissions.AllowAny,))
class UserLoginAPI(viewsets.ViewSet):

    def create(self, request, format=None):
        uname = request.data.get("uname", None)
        password = request.data.get("pwd", None)
        login_user = authenticate(username=uname, password=password)
        if login_user is not None:
            Token.objects.filter(user=login_user).delete()
            token_key = Token.objects.create(user=login_user).key
            response_data = {}
            response_data["st"] = ApiStatusCodes.OK
            response_data["scrt_key"] = token_key
            return Response(response_data)
        else:
            return Response({"st": ApiStatusCodes.AUTH_FAILED})


@permission_classes((permissions.IsAuthenticated,))
class PlayerLogoutAPI(viewsets.ViewSet):

    def create(self, request, format=None):
        Token.objects.filter(user=request.user).delete()
        return Response({"st": ApiStatusCodes.OK})