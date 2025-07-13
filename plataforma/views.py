from django.http import HttpResponse
from django.shortcuts import render
from .models import Juego, Jugador, Torneo, Participacion

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo ")

def juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juego.html', {
        "juegos": juegos
    })

def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugador.html', {
        "jugadores": jugadores
    })


def torneos(request):
    torneos = Torneo.objects.all()
    return render(request, 'torneo.html', {
        "torneos": torneos
    })

def Participacion(request):
    participacions = Participacion.objects.all()
    return render(request, 'categoria.html', {
        "participacions": participacions
    })

