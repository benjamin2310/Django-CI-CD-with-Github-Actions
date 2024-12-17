from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from .models import TravelPackage
from .serializers import TravelPackageSerializer

class TravelPackageViewSet(ModelViewSet):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer



# def home(request):
#     return HttpResponse("<h1>Welcome to Wave Travel API</h1><p>Navigate to <a href='/api/'>/api/</a> for the API endpoints.</p>")
