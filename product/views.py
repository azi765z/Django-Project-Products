from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import ProductModel
from .serializer import ProductsSerializer
from .permissions import IsSellerRole


class ProductViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductsSerializer


    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [
            IsAuthenticated(),
            IsSellerRole()
        ]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)