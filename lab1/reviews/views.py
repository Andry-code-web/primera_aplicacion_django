from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm

from asgiref.sync import sync_to_async

# Create your views here.

def index(request):
    params = {}
    return render(request, 'index.html', params)

def list_reviews(request):
    reviews = Review.objects.all()
    params = {'reviews': reviews}
    return render(request, 'list_reviews.html', params)

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_reviews')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

async def delete_review(request, review_id):
    await sync_to_async(Review.objects.filter(id=review_id).delete)()
    return redirect('list_reviews')