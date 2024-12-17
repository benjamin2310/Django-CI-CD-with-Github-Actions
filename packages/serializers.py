from rest_framework import serializers
from .models import TravelPackage

class TravelPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPackage
        fields = '__all__'
