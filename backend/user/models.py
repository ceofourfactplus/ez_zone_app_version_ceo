from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # is_email_verify = models.BooleanField(default=False)
    # is_pos_user = models.BooleanField(default=False)
    pass