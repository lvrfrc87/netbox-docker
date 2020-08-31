from extras.reports import *
from netbox_vespa_plugin.models import Vespa

name = "Vespa-related reports"

class VespaReport(Report):
    description = "Validate that every Vespa has a colour"

    def test_colour(self):
        for vespa in Vespa.objects.all():
            if vespa.colour:
                self.log_success(vespa, f"The {vespa.vespa_model} colour is {vespa.colour}")
            else:
                self.log_failure(vespa, f"The {vespa.vespa_model} needs to be painted!")

reports = [VespaReport]