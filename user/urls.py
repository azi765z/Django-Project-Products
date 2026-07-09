from django.urls import path
from .views import RegisterView, LoginView,MyProduct,UserListView,UserRoleChangeView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("my_product/", MyProduct.as_view(), name="my_product"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserRoleChangeView.as_view(), name="user_role_change"),
    
]