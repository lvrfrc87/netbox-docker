from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.RandomVespaView.as_view(), name='random_vespas'),
]
