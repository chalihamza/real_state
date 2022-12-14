# Generated by Django 4.0.2 on 2022-03-01 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house_property',
            name='Rent',
        ),
        migrations.AddField(
            model_name='house_property',
            name='Amenities',
            field=models.CharField(choices=[('Balcony', 'Balcony'), ('Deck', 'Deck'), ('Parking', 'Parking'), ('Outdoor Kitchen', 'Outdoor Kitchen'), ('Tennis Courts', 'Tennis Courts'), ('Sun Room', 'Sun Room'), ('Cable Tv', 'Cable Tv'), ('Internet', 'Internet'), ('Garden', 'Garden'), ('Concrete Flooring', 'Concrete Flooring')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='house_property',
            name='Location',
            field=models.CharField(default=111, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house_property',
            name='Property_ID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house_property',
            name='Property_Type',
            field=models.CharField(choices=[('house', 'house'), ('shop', 'shop')], default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house_property',
            name='Status',
            field=models.CharField(choices=[('PU', 'punjab'), ('KPK', 'khyber pukhtankhwa'), ('BL', 'blochistan'), ('FD', 'fedral Territory'), ('SN', 'sindh'), ('KS', 'kashmir')], default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house_property',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
