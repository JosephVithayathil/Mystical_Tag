"""Error code enums for apis."""
from .custom_enums_classes import CustomIntEnum

class ApiStatusCodes(CustomIntEnum):
    """ Api status codes."""

    OK = 0
    ERROR = 1
    DUPLICATE_USERNAME = 2
    AUTH_FAILED = 3
