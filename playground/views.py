from django.shortcuts import render
from django.http import HttpResponse
from .forms import LocationForm

def collect_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        #if form.is_valid():

    else:
        form = LocationForm()

    return render(request, 'collect_location.html', {'form': form})

def getlocationView(request):
    return render(request, 'getlocation.html')

def say_hello(request):
    return render(request, 'hello.html', {'name' : 'mosh'})
