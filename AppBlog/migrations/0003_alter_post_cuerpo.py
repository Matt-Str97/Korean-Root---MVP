# Generated by Django 4.0.4 on 2022-04-21 21:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_imagencarrusel_productoestrella_post_fuente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
