from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the home page.")

def movie(request):
    data = {
    "movies" : [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010},
        {"title": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "year": 1999},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014}
    ]}
    return render(request, 'movies/movie.html', data)

