# Generated by Django 3.0.8 on 2020-08-12 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vespa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('vespa_model', models.CharField(max_length=50)),
                ('construction_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1946, message='First Vespa made in 1946'), django.core.validators.MaxValueValidator(2020, message='Last Vespa made in 1989')])),
                ('number_of_wheels', models.PositiveIntegerField(default=3)),
                ('colour', models.CharField(max_length=50)),
                ('gear', models.PositiveIntegerField(default=3)),
                ('nuts_per_wheel', models.PositiveIntegerField(default=4)),
            ],
            options={
                'ordering': ['construction_year'],
            },
        ),
    ]
