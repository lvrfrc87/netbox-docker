from extras.plugins import PluginConfig

class VespaModelsConfig(PluginConfig):
    name = 'netbox_vespa_plugin'
    verbose_name = 'Vespa Models'
    description = 'An example plugin for development purposes'
    version = '0.1'
    author = 'Federico Olivieri'
    author_email = 'lvrfrc87@gmail.com'
    required_settings = []
    default_settings = {}
    base_url = 'vespa-models'
    caching_config = {}


config = VespaModelsConfig
