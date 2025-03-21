# Generated by Django 5.1.6 on 2025-03-03 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('max_hours_per_week', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10, unique=True)),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('departure_time', models.DateTimeField()),
                ('duration_hours', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.crewmember')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.flight')),
            ],
        ),
    ]
