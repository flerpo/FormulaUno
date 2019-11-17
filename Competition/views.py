from django.http import request
from django.shortcuts import render
# Create your views here.
from rest_framework import generics

from Competition.models import Tracks
from Competition.serializers import TrackSerializer


def tracks(request):
    return render(request, 'tracks.html', {'tracks': Tracks.objects.all()})


class ListTracks(generics.ListCreateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TrackSerializer


class DetailTrack(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TrackSerializer
