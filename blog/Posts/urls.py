from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("blog/<slug>", views.blog, name="blog_View"),
    path("blog/", views.postBlog, name="Post blog"),
    path("edit/<slug>", views.editBlog, name="edit blog"),
]

