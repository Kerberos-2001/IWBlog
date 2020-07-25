from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.forms import ValidationError

User = get_user_model()


class UserEmailBackends(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError("Invalid email or password")

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
