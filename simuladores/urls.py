from django.urls import path
from . import views

app_name = 'simuladores'

urlpatterns = [
    path('', views.portal, name='portal'),
    path('espectro/', views.espectro, name='espectro'),
    path('canais/', views.canais_wifi, name='canais_wifi'),
    path('mapa-calor/', views.mapa_calor, name='mapa_calor'),
    path('diafonia/', views.diafonia, name='diafonia'),
    path('atenuacao/', views.atenuacao, name='atenuacao'),
    path('emi-industrial/', views.emi_industrial, name='emi_industrial'),
    path('retransmissor/', views.Recuperacao_de_erros, name='retransmissor'),
]