import os

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
        "ENGINE": os.environ["SCOOP_DATABASE_ENGINE"],
        "NAME": os.environ["SCOOP_DATABASE_NAME"],
        "USER": os.environ["SCOOP_DATABASE_USER"],
        "PASSWORD": os.environ["SCOOP_DATABASE_PASSWORD"],
        "HOST": os.environ["SCOOP_DATABASE_HOST"],
        "PORT": os.environ["SCOOP_DATABASE_PORT"],
    }
}
