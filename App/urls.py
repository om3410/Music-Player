from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/songs/", views.songs_api, name="songs_api"),  # API endpoint for songs
]