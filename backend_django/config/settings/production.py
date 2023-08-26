from .base import *

DEBUG = False


ALLOWED_HOSTS = []


CUSTOM_APPS = [
    "apps.users",
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS + THIRD_PARTY_APPS


DATABASES = {
    "default": {
        "ENGINE": get_env_variable("SCOOP_DATABASE_ENGINE"),
        "NAME": get_env_variable("SCOOP_DATABASE_NAME"),
        "USER": get_env_variable("SCOOP_DATABASE_USER"),
        "PASSWORD": get_env_variable("SCOOP_DATABASE_PASSWORD"),
        "HOST": get_env_variable("SCOOP_DATABASE_HOST"),
        "PORT": get_env_variable("SCOOP_DATABASE_PORT"),
    }
}
