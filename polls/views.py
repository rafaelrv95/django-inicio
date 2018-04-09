from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, world. estoy en el index de polls")

# Create your views here.
