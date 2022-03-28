from core import views
from django.urls import path

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('dashboard', views.dashboard, name='dashboard'),
]