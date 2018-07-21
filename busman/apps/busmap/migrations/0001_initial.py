# Generated by Django 2.0.7 on 2018-07-21 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=30, unique=True)),
                ('space', models.CharField(blank=True, max_length=4)),
                ('bus_number', models.CharField(blank=True, max_length=5)),
                ('status', models.CharField(choices=[('a', 'Arrived (In the lot)'), ('d', 'Delayed'), ('o', 'On Time (Expected)')], default='o', max_length=1, verbose_name='arrival status')),
            ],
        ),
        migrations.CreateModel(
            name='UserBusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_bus_admin', models.BooleanField(default=False)),
                ('route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='busmap.Route')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
