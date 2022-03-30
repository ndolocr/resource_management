from django.shortcuts import render

from house.models import Plot
# Create your views here.

def view_all_plots(request):
    plots = Plot.objects.all()
    
    context = { "plots": plots }
    return render(request, "house/all-plots.html", context)

def view_all_houses(request):
    pass

def view_all_rooms(request):
    pass

def view_all_room_types(request):
    pass

def view_all_house_types(request):
    pass

def view_all_tenants(request):
    pass

def view_single_house(request):
    pass

def view_single_plot(request):
    pass

def view_single_room(request):
    pass

def view_single_tenant(request):
    pass