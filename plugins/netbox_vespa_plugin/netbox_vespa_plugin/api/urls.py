from rest_framework import routers
from .views import VespaViewSet

router = routers.DefaultRouter()
router.register('vespas', VespaViewSet)
urlpatterns = router.urls