from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django_resized import ResizedImageField


class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    dob = models.DateField(blank=True, null=True)
    profilepic = models.ImageField(upload_to="profile", blank=True, null=True)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    slug = models.SlugField(blank=True, null=True)
    image = ResizedImageField(
        size=[600, 300], upload_to="thumbnail", blank=True, null=True
    )
    created_at = models.DateField(auto_now_add=True, editable=True)
    updated_at = models.DateField(auto_now=True, editable=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image == None:
            self.image = "profile/contact.png"
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


def slugfield(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slugfield, sender=Blog)
