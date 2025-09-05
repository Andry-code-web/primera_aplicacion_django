from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_reviews, name='list_reviews'),
    path('add/', views.add_review, name='add_review'),
]