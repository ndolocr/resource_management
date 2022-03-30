from django.urls import path

from house import views

urlpatterns =[
    path('plot/', views.view_all_plots, name='all-plots'),
]