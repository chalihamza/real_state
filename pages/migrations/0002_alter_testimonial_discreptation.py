# Generated by Django 4.0.2 on 2022-03-01 05:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='discreptation',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
