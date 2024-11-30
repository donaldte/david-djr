# Generated by Django 5.1.3 on 2024-11-30 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0002_hotel_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='price_per_night',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
