# Generated by Django 2.0.5 on 2018-08-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img/items', verbose_name='Imagen del articulo'),
        ),
    ]
