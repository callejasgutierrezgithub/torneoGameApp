from django.contrib import admin
from .models import Juego, Jugador, Torneo, Participacion

class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'creador', 'created_at')
    ordering = ('titulo',)
    search_fields = ('titulo',)  
admin.site.register(Juego, JuegoAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'pais', 'created_at')
    ordering = ('pais',)
    search_fields = ('pais',)  
admin.site.register(Jugador, JugadorAdmin)

class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'juego_titulo')
    ordering = ('nombre',)
    search_fields = ('nombre',)  
    def juego_titulo(self, obj):
        return obj.juego.titulo
    juego_titulo.short_description = 'Juego'
   
admin.site.register(Torneo, TorneoAdmin)

class ParticipacionAdmin(admin.ModelAdmin):
    list_display = ('jugador_nickname', 'torneo_nombre', 'puntaje_final', 'created_at')    
    ordering = ('torneo__nombre',)
    search_fields = ('jugador__nickname',) 
    def jugador_nickname(self, obj):
        return obj.jugador.nickname
    jugador_nickname.short_description = 'Jugador'
    def torneo_nombre(self, obj):
        return obj.torneo.nombre
    torneo_nombre.short_description = 'Torneo'

admin.site.register(Participacion, ParticipacionAdmin)