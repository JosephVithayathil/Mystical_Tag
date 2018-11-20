"""Client rest api urls."""
from rest_framework.routers import SimpleRouter
from .apis import signup, login


urlpatterns = [
]
router = SimpleRouter(trailing_slash=False)

# Signup API's
router.register(r'user_signup_api', signup.UserSignupAPI, "user_signup_api")
router.register(r'user_name_check_api', signup.UserNameCheckAPI, "user_name_check_api")

# Login API's
router.register(r'user_login_api', login.UserLoginAPI, "user_login_api")
router.register(r'user_logout_api', login.UserLoginAPI, "user_logout_api")

urlpatterns += router.urls