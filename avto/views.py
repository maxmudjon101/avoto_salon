from django.shortcuts import render
from .serializers import avtomobilSerializer
from .models import Avtosalon
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView



class avtomobilViewSet(ModelViewSet):
    queryset = Avtosalon.objects.all()
    serializer_class = avtomobilSerializer

def malumot(request):
    return render(request,'404.html')


def aboutwivs(request):
    return render(request,'about.html')


def boking(request):
    return render(request,'booking.html')


def aloqa(request):
    return render(request,'contact.html')


def home(request):
    return render(request,'index.html')


def sevicewivs(request):
    return render(request,'service.html')


def team(request):
    return render(request,'team.html')

def testimonital(request):
    return render(request,'testimonial.html')