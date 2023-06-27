from django.shortcuts import render

def index(request):
    context={}
    return render(request, 'pages/index.html', context)

def login(request):
    context={}
    return render(request, 'pages/login.html', context)

def form1(request):
    context={}
    return render(request, 'pages/form1.html', context)

def plants(request):
    context={}
    return render(request, 'pages/plants.html', context)

# Create your views here.
