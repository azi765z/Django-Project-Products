from rest_framework import viewsets
from .serializer import SubCategorySerializer
from .models import SubCategoryModel

# Create your views here.

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategoryModel.objects.all()
    serializer_class = SubCategorySerializer
