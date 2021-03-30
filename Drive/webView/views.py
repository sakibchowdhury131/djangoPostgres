from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageView

# Create your views here.

def index(request):
    imgs = ImageView.objects.all()
    return render(request, 'index.html', {'imgs' : imgs})
