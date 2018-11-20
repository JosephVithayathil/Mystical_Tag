"""Apis for user create and signup."""
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from common_library.status_codes import ApiStatusCodes


@permission_classes((permissions.AllowAny,))
class UserSignupAPI(viewsets.ViewSet):
    """Api for user sign up."""

    def create(self, request, format=None):
        """POST function."""
        uname = request.data.get("uname", None)
        password = request.data.get("pwd", None)
        email = request.data.get("email", None)
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("first_name", None)
        if None in [uname, email, first_name, last_name]:
            return Response({"st": ApiStatusCodes.ERROR})
        if User.objects.filter(username=uname).count() > 0:
            return Response({"st": ApiStatusCodes.DUPLICATE_USERNAME})
        user = User.objects.create_user(
            username=uname,
            password=password,
            email=email
        )
        token_key = Token.objects.create(user=user).key
        response_data = {}
        response_data["st"] = ApiStatusCodes.OK
        response_data["scrt_key"] = token_key
        return Response(response_data)



@permission_classes((permissions.AllowAny,))
class UserNameCheckAPI(viewsets.ViewSet):
    """Api for username check."""

    def create(self, request, format=None):
        """POST function."""
        uname = request.data.get("uname", None)
        if None in [uname]:
            return Response({"st": ApiStatusCodes.ERROR})
        if User.objects.filter(username=uname).count() > 0:
            return Response({"st": ApiStatusCodes.DUPLICATE_USERNAME})
        return Response({"st": ApiStatusCodes.OK})
