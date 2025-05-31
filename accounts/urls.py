# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('vuln/', views.vuln, name='vuln'),
]