from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

user = get_user_model()


class User(AbstractUser):
    email = models.EmailField(blank=False)
    dob = models.DateField()
    profilepic = models.ImageField(upload_to="profile")
