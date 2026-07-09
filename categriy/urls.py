from rest_framework.routers import DefaultRouter
from categriy import views

router=DefaultRouter()
router.register('categoriy',views.CategoriyViewSet,basename='categoriy')

urlpatterns=router.urls
