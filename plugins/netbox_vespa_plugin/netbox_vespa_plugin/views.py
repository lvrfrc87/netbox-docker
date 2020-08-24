from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import Vespa

class RandomVespaView(View):
    def get(self, request):
        vespa = Vespa.objects.order_by('?').first()
        return render(request, 'netbox_vespa_plugin/vespa.html', {
            'vespa': vespa,
        })

class ListVespasView(View):
    def get(self, request):
        vespas = Vespa.objects.all()
        return render(request, 'netbox_vespa_plugin/vespa_list.html', {
            'vespas': vespas,
        })

class VespaView(View):
    def get(self, request, vespa_model):
        vespa = get_object_or_404(Vespa.objects.filter(vespa_model=vespa_model))
        return render(request, 'netbox_vespa_plugin/vespa.html', {
            'vespa': vespa,
        })

