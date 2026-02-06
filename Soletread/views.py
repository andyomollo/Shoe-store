from django.shortcuts import render
from django.http import HttpResponse
from .models import Sneaker

# Create your views here.
def index(request):
    sneakers = Sneaker.objects.all()
    context = {
        "sneakers": sneakers
    }
    return render(request, "Soletread/index.html", context)