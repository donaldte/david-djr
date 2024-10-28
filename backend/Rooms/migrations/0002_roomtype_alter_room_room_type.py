# Generated by Django 5.1.2 on 2024-10-23 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0001_initial'),
        ('Rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('price_start', models.DecimalField(decimal_places=2, max_digits=7)),
                ('price_end', models.DecimalField(decimal_places=2, max_digits=7)),
                ('beds_num', models.PositiveIntegerField()),
                ('room_size', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room_type', to='Hotels.hotel')),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_type', to='Rooms.roomtype'),
        ),
    ]