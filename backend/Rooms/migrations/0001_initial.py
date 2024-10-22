# Generated by Django 5.1.2 on 2024-10-22 09:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hotels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('capacity', models.IntegerField()),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('is_available', models.BooleanField()),
                ('room_type', models.CharField(choices=[('SIMPLE', 'simple'), ('DOUBLE', 'double'), ('VIP', 'vip')])),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotels.hotel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
