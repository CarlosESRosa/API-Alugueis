from django.urls import path, include
from .views import ImovelListApiView, ImovelDetailApiView, AnuncioListApiView, ReservaListApiView, AnuncioDetailApiView, ReservaDetailApiView

urlpatterns = [
    path('imovel', ImovelListApiView.as_view()),
    path('imovel/<imovel_id>', ImovelDetailApiView.as_view()),
    path('anuncio', AnuncioListApiView.as_view()),
    path('anuncio/<anuncio_id>', AnuncioDetailApiView.as_view()),
    path('reserva', ReservaListApiView.as_view()),
    path('reserva/<reserva_id>', ReservaDetailApiView.as_view()),
]