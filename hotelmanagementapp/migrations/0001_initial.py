# Generated by Django 5.0.2 on 2024-04-05 14:48

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('is_available', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('admin_decision', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('medical_history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagementapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagementapp.patient')),
            ],
        ),
    ]
