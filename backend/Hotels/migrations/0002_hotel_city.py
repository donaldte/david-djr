# Generated by Django 5.1.3 on 2024-11-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]