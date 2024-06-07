from django.urls import path
from . import views

urlpatterns = [
    path('setor/', views.setor, name='setor'),
]   