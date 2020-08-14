from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Vespa(models.Model):

    GEAR_CHOISES = (
        (3, 'Three'),
        (4, 'Four')
    )

    NUTS_CHOISES = (
        (4, 'Four'),
        (5, 'Five')
    )

    WHEELS_CHOISES = (
        (2, 'Two'),
        (3, 'Two + Spare')
    )

    vespa_model         = models.CharField(max_length=50)
    construction_year   = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1946, message='First Vespa made in 1946'), 
            MaxValueValidator(2020, message='Last Vespa made in 1989'),
            ]
        )
    number_of_wheels    = models.PositiveIntegerField(default=3,choices=WHEELS_CHOISES)
    colour              = models.CharField(max_length=50)
    gear                = models.PositiveIntegerField(default=3,choices=GEAR_CHOISES)
    nuts_per_wheel      = models.PositiveIntegerField(default=4,choices=NUTS_CHOISES)         

    class Meta:
        ordering = ['construction_year']

    def __str__(self):
        return self.vespa_model