from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'login/sesion.html')

# Create your views here.
