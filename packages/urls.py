from rest_framework.routers import DefaultRouter
from .views import TravelPackageViewSet

router = DefaultRouter()
router.register(r'packages', TravelPackageViewSet, basename='travelpackage')

urlpatterns = router.urls
