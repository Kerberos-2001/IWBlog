from django import forms
from django.contrib.auth import authenticate, get_user_model


USER = get_user_model()


class Login(forms.Form):
    email = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Email or Username"}
        ),
    )
    password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Password"}),
    )


class Resgister(forms.Form):
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "First Name"}),
    )

    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Last Name"}),
    )

    email = forms.EmailField(
        max_length=200,
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": "Email"}),
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "input", "placeholder": "Username"}),
    )

    password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Email"}),
    )

    confrom_password = forms.CharField(
        max_length=200,
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "Confirm Password"}
        ),
    )

    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "input", "placeholder": "Date Of Birth"})
    )

    def clean_username(self):
        if USER.objects.filter(username=self.cleaned_data["username"]).exists():
            raise forms.ValidationError("Username is already taken")
        return self.cleaned_data["username"]

    def clean(self):
        password = self.cleaned_data["password"]
        conPassword = self.cleaned_data["confrom_password"]
        if password != conPassword:
            raise forms.ValidationError("Password didnt match")

