from rest_framework.routers import DefaultRouter
from sub_categriy import views
from .views import SubCategoryViewSet


router=DefaultRouter()
router.register('sub_categriy',views.SubCategoryViewSet,basename='sub_categriy')

urlpatterns=router.urls