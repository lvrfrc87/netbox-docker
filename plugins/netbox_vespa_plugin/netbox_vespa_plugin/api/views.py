from rest_framework.viewsets import ModelViewSet
from netbox_vespa_plugin.models import Vespa
from .serializers import VespaSerializer

class VespaViewSet(ModelViewSet):
    queryset = Vespa.objects.all()
    serializer_class = VespaSerializer