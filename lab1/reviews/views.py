from django.shortcuts import render
from .models import Review

# Create your views here.

def index(request):
    params = {}
    return render(request, 'index.html', params)

def list_reviews(request):
    reviews = Review.objects.all()
    params = {'reviews': reviews}
    return render(request, 'list_reviews.html', params)