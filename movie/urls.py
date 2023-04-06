from django.urls import path

from movie import views


urlpatterns = [
    path("", views.MovieViews.as_view()),
]