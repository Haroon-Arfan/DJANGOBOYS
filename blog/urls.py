from django.urls import path
from . import views

# Urls for the blog page are below

urlpatterns = [
    path('', views.post_list, name="post_list")
]
