from extras.scripts import *
from netbox_vespa_plugin.models import Vespa

name = "Vespa-related scripts"

class VespaScript(Script):
    class Meta:
        description = "How old is this Vespa?"

    vespa = StringVar()

    def run(self, data, commit):
        try:
            vespa = Vespa.objects.get(vespa_model=data['vespa_model'])
            self.log_success(f'The {vespa.vespa_model} is "{2020 - int(vespa.construction_year)}"years old!')
        except Vespa.DoesNotExist:
            self.log_failure(f'No such Vespa "{data["animal"]}"')

scripts = [VespaScript]