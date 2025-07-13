from django.urls import path
from . import views

urlpatterns = [    
    path('juegos/', views.juegos),
    path('jugadores/', views.jugadores),
    path('torneos/', views.torneos),
]

