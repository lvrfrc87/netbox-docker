from django.contrib import admin
from .models import Vespa

@admin.register(Vespa)
class VespaAdmin(admin.ModelAdmin):
    list_display = (
        'vespa_model', 
        'construction_year', 
        'number_of_wheels',
        'colour',
        'gear',
        'nuts_per_wheel'
        )

    list_filter = (
        'construction_year',
    )

    search_fields = (
        'construction_year', 
        'gear',
        'nuts_per_wheel',
    )