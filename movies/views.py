from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie


def home(request):
    return HttpResponse("Welcome to the home page.")

def movie(request):
    # data = {
    # "movies" : [
    #     {"title": "Inception", "director": "Christopher Nolan", "year": 2010},
    #     {"title": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "year": 1999},
    #     {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014}
    # ]}
    data = Movie.objects.all()

    return render(request, 'movies/movie.html', {'movies': data})



def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})