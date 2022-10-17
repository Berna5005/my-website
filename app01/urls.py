from django.urls import path
from . import views

urlpatterns = [
path('berna5005.eu.pythonanywhere.com', views.Register_view, name = 'register'),
]