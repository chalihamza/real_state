# Generated by Django 4.0.2 on 2022-03-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_house_property_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_property',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
