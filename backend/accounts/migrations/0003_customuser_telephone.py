# Generated by Django 5.1.2 on 2024-11-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_code_customuser_is_phone_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telephone',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]