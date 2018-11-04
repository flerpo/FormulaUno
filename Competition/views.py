from django.http import request
from django.shortcuts import render
# Create your views here.
from Competition.models import Tracks


def tracks(request):
    return render(request, 'index.html', {'tracks': Tracks.objects.all()})

