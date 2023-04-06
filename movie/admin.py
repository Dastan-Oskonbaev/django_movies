from django.contrib import admin

from .models import Category, Actor, RatingStar, Rating, Movie, MovieShorts, Genre, Reviews
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(MovieShorts)
admin.site.register(Genre)
admin.site.register(Reviews)
