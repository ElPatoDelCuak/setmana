from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personatge/', views.personatge, name='personatge'),
]