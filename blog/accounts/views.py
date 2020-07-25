from django.shortcuts import render, redirect
from .forms import *
from .backends import UserEmailBackends
from django.contrib.auth import login, get_user_model
from django.core.mail import send_mail
from blog.settings import EMAIL_HOST_USER
from django.forms import ValidationError

# Create your views here.


def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            auth = UserEmailBackends()
            userobj = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(request, username=userobj, password=password)
            if user is not None:
                login(request, user)
                redirect("/")
            else:
                raise ValidationError("Your are not registered")

    form = Login()
    context = {}
    context["form"] = form
    return render(request, "accounts/login.html", context)


def register(request):
    if request.method == "POST":
        form = Resgister(request.POST)
        if form.is_valid():
            user = get_user_model()
            fname = form.cleaned_data["first_name"]
            lname = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            dob = form.cleaned_data["birth_date"]
            uname = form.cleaned_data["username"]

            obj = user(
                username=uname, first_name=fname, last_name=lname, email=email, dob=dob,
            )
            obj.set_password(password)
            obj.save()
            auth = UserEmailBackends()
            signUpobj = auth.authenticate(request, username=email, password=password)
            if signUpobj is not None:
                subject = "Welcome to our web page"
                message = "You have successfully signed up to our web page"
                from_email = EMAIL_HOST_USER
                recipient_list = [
                    email,
                ]
                send_mail(subject, message, from_email, recipient_list)
                print("email sent")
                login(request, signUpobj)
                redirect("/")
            else:
                raise ValidationError("You might not be registered yet")

    form = Resgister()
    context = {}
    context["form"] = form
    return render(request, "accounts/register.html", context)
