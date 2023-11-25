from django.shortcuts import render
from django.http import HttpResponse

def homepageView(request):
    return render(request, 'button.html')

def lieu1(request):
     return render(request, 'lieu1.html')

def lieu2(request):
    return render(request, 'lieu2.html')

# def say_hello(request):
#     return render(request, 'hello.html', {'name' : 'mosh'})
