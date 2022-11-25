from django.urls import path, include
from .views import ImovelListApiView, ImovelDetailApiView

urlpatterns = [
    path('api', ImovelListApiView.as_view()),
    path('api/<imovel_id>/', ImovelDetailApiView.as_view()),
]