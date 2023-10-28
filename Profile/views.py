from django.shortcuts import render
from .models import User, Trait
  
# Create your views here.

def index(request):
    data = User.objects.all()
    return render(request, 'index.html', {'data':data})

def new(request):
    newData = Trait.objects.all()
    return render(request, 'new.html', {'newData':newData})