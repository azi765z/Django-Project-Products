from django.shortcuts import render
from rest_framework import viewsets

from .models import CategoriyModel
from .serializer import CategoriySerializer
# Create your views here.

class CategoriyViewSet(viewsets.ModelViewSet):
    queryset = CategoriyModel.objects.all()
    serializer_class = CategoriySerializer