# Generated by Django 4.0.2 on 2022-03-03 10:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_blognews_discreptation_blognews_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='blognews',
            name='about_writer',
            field=ckeditor.fields.RichTextField(default=1),
        ),
    ]
