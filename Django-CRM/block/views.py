from django.shortcuts import redirect, render
from .models import *
from .forms import Registration

def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("/")
    else:
        form = Registration()
        
    return render(request, "form.html", {"form": form})
