from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class User(AbstractUser):
    user_role = models.CharField('user_role', max_length=200, default='user')
