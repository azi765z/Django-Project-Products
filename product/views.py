from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from product.serializer import ProductsSerializer
from .models import ProductModel
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    def perferom_create(self,serializer):
        serializer.save(user=self.request.user)
        
