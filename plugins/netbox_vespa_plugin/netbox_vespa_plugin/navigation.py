from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_vespa_plugin:random_vespas',
        link_text='List all vespas',
        permissions=[],
        buttons=(

            PluginMenuButton(
                link='plugins:netbox_vespa_plugin:random_vespas', 
                title='Vespa', 
                icon_class='fa fa-info', 
                color=ButtonColorChoices.BLUE
                ),

            PluginMenuButton(
                link='admin:netbox_vespa_plugin_vespa_add', 
                title='Add Vespa', 
                icon_class='fa fa-plus', 
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_vespa_plugin.vespa_add']
                ),

            # PluginMenuButton(
            #     link='vespas', 
            #     title='API', 
            #     icon_class='fa fa-minus', 
            #     color=ButtonColorChoices.RED
            #     ),
        )
    ),
)