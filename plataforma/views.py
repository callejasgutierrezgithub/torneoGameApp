from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Juego, Jugador, Torneo, Participacion
from .forms import JugadorForm

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo ")

def juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juego.html', {
        "juegos": juegos
    })

def form_juego(request):
    juegos = Juego.objects.all()
    post_titulo = request.POST.get('titulo')
    post_genero = request.POST.get('genero')
    post_creador = request.POST.get('creador')
    if post_titulo:
        q = Juego(titulo=post_titulo, genero=post_genero, creador=post_creador)
        q.save()

    return render(request, 'form_juego.html', {
        "juegos": juegos
    })


def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugador.html', {
        "jugadores": jugadores
    })

def form_jugador(request):
    form = JugadorForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'form_jugador.html', {
        "form": form
    })

def torneos(request):
    torneos = Torneo.objects.all()
    return render(request, 'torneo.html', {
        "torneos": torneos
    })

def participacion(request):
    participacions = Participacion.objects.all()
    return render(request, 'participacion.html', {
        "participacions": participacions
    })


