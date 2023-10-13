from django.urls import path
from . import views

urlpatterns = [
    path('', views.makoRS, name="makoRS"),
    path('', views.commonsRS, name="commonsRS"),
    path('', views.leogoodwinRS, name="leogoodwinRS"),
    path('', views.clcRS, name="clcRS"),
    path('', views.vettelRS, name="vettelRS"),
    path('', views.farquharRS, name="farquharRS"),
    path('', views.foundersRS, name="foundersRS"),
    path('', views.rollingRS, name="rollingRS"),
]
