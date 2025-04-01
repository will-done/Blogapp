from django.urls import path
from . import views
# http://127.0.0.1:8000/          = index
# http://127.0.0.1:8000/index     = index
# http://127.0.0.1:8000/ blogs    = blogs
# http://127.0.0.1:8000/blogs/3   = index


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>",views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details, name="blogs_details"),

]