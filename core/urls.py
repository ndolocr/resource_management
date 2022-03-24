from core import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='index-page'),
]