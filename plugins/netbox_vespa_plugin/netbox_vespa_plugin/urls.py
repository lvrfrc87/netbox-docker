from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.RandomVespaView.as_view(), name='random_vespas'),
    path('', views.ListVespasView.as_view(), name='list_vespa'),
    path('<str:vespa_model>/', views.VespaView.as_view(), name='vespa_model'),
]
