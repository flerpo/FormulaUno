from rest_framework import serializers
from .models import Tracks


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'trackId',
            'name',
            'location',
        )
        model = Tracks