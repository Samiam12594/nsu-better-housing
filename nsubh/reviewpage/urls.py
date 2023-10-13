from django.urls import path

from . import views

# Creates route to the review page
urlpatterns = [
    path('', views.reviewpage, name='reviewpage'),
]
