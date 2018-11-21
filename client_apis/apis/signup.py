"""Apis for user create and signup."""
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from common_library.status_codes import ApiStatusCodes


@permission_classes((permissions.AllowAny,))
class UserSignupAPI(viewsets.ViewSet):
    """API for user signup.
       Input:
        1. uname : User Name
        2. pwd : Password
        3. email : Email
        4. first_name : First Name
        5. last_name : First Name
       Output:
        1. st: Status
        2. scrt_key: Secret Key that should be appended on the header as Autherisation token.
    """

    def create(self, request, format=None):
        """POST function."""
        uname = request.data.get("uname", None)
        password = request.data.get("pwd", None)
        email = request.data.get("email", None)
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)
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
    """API for user username availabily check.
       Input:
        1. uname : User Name
       Output:
        1. st: Status
    """

    def create(self, request, format=None):
        """POST function."""
        uname = request.data.get("uname", None)
        if None in [uname]:
            return Response({"st": ApiStatusCodes.ERROR})
        if User.objects.filter(username=uname).count() > 0:
            return Response({"st": ApiStatusCodes.DUPLICATE_USERNAME})
        return Response({"st": ApiStatusCodes.OK})
