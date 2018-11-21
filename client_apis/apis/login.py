"""Apis for player signup."""
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from common_library.status_codes import ApiStatusCodes


@permission_classes((permissions.AllowAny,))
class UserLoginAPI(viewsets.ViewSet):
    """API for login.
       Input:
        1. uname : User Name
        2. pwd : Password
       Output:
        1. st: Status
        2. scrt_key: Secret Key that should be appended on the header as Autherisation token.
    """

    def create(self, request, format=None):
        """POST api."""
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
    """API for logout.
       Input:
        "Empty"
       Output:
        1. st: Status
    """
    def create(self, request, format=None):
        """POST api."""
        Token.objects.filter(user=request.user).delete()
        return Response({"st": ApiStatusCodes.OK})
