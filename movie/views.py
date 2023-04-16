from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

import movie
from .forms import  ReviewForm
from .models import Movie, Category, Actor


class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movie_movies.html"


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    model = Actor
    template_name = 'movie/actor.html'
    slug_field = 'name'