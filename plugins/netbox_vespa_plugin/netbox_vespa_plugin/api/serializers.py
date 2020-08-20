from rest_framework.serializers import ModelSerializer
from netbox_vespa_plugin.models import Vespa

class VespaSerializer(ModelSerializer):

    class Meta:
        model = Vespa
        fields = (
            'vespa_model',
            'construction_year',
            'number_of_wheels',
            'colour',
            'gear',
            'nuts_per_wheel'
            )