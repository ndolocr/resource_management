from multiprocessing import context
from django.contrib import messages

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username, password)

        if user is not None:
            login(request, user)
            return redirect('dasboard')
        else:
            messages.success(request, ("Invalid login credentials!"))
            return redirect('login')
    else:        
        context={}
        return render(request, 'core/login.html', context)

def dashboard(request):
    return render(request, 'core/dashboard.html')

