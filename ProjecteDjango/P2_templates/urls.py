from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('<str:personatge>/', views.personatge, name='personatge'),
    # Ruta per a personatge específic
]