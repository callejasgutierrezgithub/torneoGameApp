from django.urls import path
from . import views

urlpatterns = [    
    path('juegos/', views.juegos),
    path('jugadores/', views.jugadores),
    path('torneos/', views.torneos),
    path('participacion/', views.participacion),
    path('form_juego/', views.form_juego, name='juegos'),
    path('form_jugador/', views.form_jugador, name='jugador'),
]

