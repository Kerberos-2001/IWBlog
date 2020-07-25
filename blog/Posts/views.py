from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import blogForm


def index(request):
    context = {}
    blogs = Blog.objects.all()
    print(blogs)
    context["blogs"] = blogs
    return render(request, "Posts/index.html", context)


def blog(request, slug):
    context = {}
    blogC = Blog.objects.get(slug=slug)
    context["blog"] = blogC
    if str(request.user) == str(blogC.user.username):
        context["isUser"] = "same"
    else:
        context["isUser"] = "notsame"
    return render(request, "Posts/blog.html", context)


@login_required
def postBlog(request):
    if request.method == "POST":
        form = blogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            thubnail = form.cleaned_data["thumbnail"]
            blogpost = Blog(user=request.user, title=title, body=body)
            if thubnail is None:
                blogpost.save()
            else:
                blogpost.image = thubnail
                blogpost.save()
    context = {}
    blog = blogForm()
    context["form"] = blog
    return render(request, "Posts/addblog.html", context)


@login_required
def editBlog(request, slug):
    if request.method == "POST":
        form = blogForm(request.POST)
        if form.is_valid():
            obj = Blog.objects.get(slug=slug)
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            image = form.cleaned_data["thumbnail"]
            obj.title = title
            if body is None:
                obj.body = obj.body
            else:
                obj.body = body
            if image is None:
                obj.save()
            else:
                obj.image = image
                obj.save()
    context = {}
    obj = Blog.objects.get(slug=slug)
    if str(request.user) == str(obj.user.username):
        title = obj.title
        body = obj.body
        image = obj.image
        blog = blogForm()
        context["form"] = blog
        context["title"] = title
        context["body"] = body
        context["image"] = image

        return render(request, "Posts/editblog.html", context)
    return render(request, "Posts/blog.html", context)
