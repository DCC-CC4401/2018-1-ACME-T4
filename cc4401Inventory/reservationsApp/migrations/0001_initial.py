# Generated by Django 2.0.5 on 2018-08-17 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spacesApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date_time', models.DateTimeField()),
                ('ending_date_time', models.DateTimeField()),
                ('state', models.CharField(choices=[('A', 'Aceptado'), ('R', 'Rechazado'), ('P', 'Pendiente')], default='P', max_length=1, verbose_name='Estado')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spacesApp.Space')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
