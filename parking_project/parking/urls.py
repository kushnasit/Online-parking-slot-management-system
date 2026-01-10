from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('slots/', views.slots, name='slots'),
    path('booking/', views.booking, name='booking'),

]
