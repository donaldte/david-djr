# Generated by Django 5.1.3 on 2024-11-24 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Commentaires', '0001_initial'),
        ('Rooms', '0004_alter_room_is_available_alter_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Rooms.room'),
        ),
    ]