from .models import Avtosalon
from rest_framework import serializers








class avtomobilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Avtosalon
        fields="__all__"