# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('vuln/', views.vuln, name='vuln'),
]