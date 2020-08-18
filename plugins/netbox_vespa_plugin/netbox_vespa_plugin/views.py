from django.shortcuts import render
from django.views.generic import View
from .models import Vespa

class RandomVespaView(View):
    def get(self, request):
        vespa = Vespa.objects.order_by('?').first()
        return render(request, 'netbox_vespa_plugin/vespa.html', {
            'vespa': vespa,
        })
