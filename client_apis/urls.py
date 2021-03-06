"""Client rest api urls."""
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from .apis import signup, login, search_films, create_edit_film
from . import views


urlpatterns = [
    # Views
    url(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view())
]
router = SimpleRouter(trailing_slash=False)

# Signup API's
router.register(r'user_signup_api', signup.UserSignupAPI, "user_signup_api")
router.register(r'user_name_check_api', signup.UserNameCheckAPI, "user_name_check_api")

# Login API's
router.register(r'user_login_api', login.UserLoginAPI, "user_login_api")
router.register(r'user_logout_api', login.UserLoginAPI, "user_logout_api")


# Search API's
router.register(r'search_api', search_films.SearchAPI, "search_api")

# Create or Edit Movies API's
router.register(r'create_edit_movie_api', create_edit_film.Create_Edit_Movie_API, "create_edit_movie_api")


urlpatterns += router.urls