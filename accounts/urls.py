# accounts/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.subscription_view, name='subscription'),
    path('login/', views.login_view, name='login'),
    path('vuln/', views.vuln, name='vuln'),
    # path('logout/', views.logout_view, name='logout'),  # Your custom logout view
    # Alternatively, use Django's built-in logout view:
    path('logout/', views.logout_view, name='logout'),
]