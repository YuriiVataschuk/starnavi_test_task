import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_login = models.DateTimeField(default=datetime.datetime.now)
    last_request = models.DateTimeField(default=datetime.datetime.now)
