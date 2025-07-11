# Generated by Django 5.2.2 on 2025-06-05 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
                ('instructor', models.CharField(max_length=100)),
                ('available_slots', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.AddField(
            model_name='booking',
            name='fitness_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fitnessclass'),
        ),
    ]
