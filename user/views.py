from rest_framework import status,generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserSerializer, LoginSerializer,UserViewserializer,UserRoleChangeSerializer
from product.serializer import ProductsSerializer
from product.models import ProductModel
from .permissions import IsAdminRole
from .models import UserModel


class UserListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserViewserializer
    permission_classes = [ IsAdminRole]
    
class UserRoleChangeView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRoleChangeSerializer
    permission_classes = [IsAdminRole]


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']    

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
                     status=status.HTTP_200_OK)

class MyProduct(ListAPIView):
    serializer_class=ProductsSerializer
    permission_classes=(IsAuthenticated)
    
    def get_queryset(self):
        return ProductModel.objects.filter(user=self.request.user)  
    
    
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
