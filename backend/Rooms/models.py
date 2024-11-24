from django.db import models
from Hotels.models import Hotel
from accounts.models import CustomUser
from django.utils.text import slugify


class RoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        related_name="hotel_room_type",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=500, default="", blank=True, null=True)
    price_start = models.DecimalField(max_digits=7, decimal_places=2)
    price_end = models.DecimalField(max_digits=7, decimal_places=2)
    beds_num = models.PositiveIntegerField()
    room_size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)





status = (('CONFIRMEE' , 'confirmee') , ('ANNULEE' , 'annulee'))
room_choices_type = (('SIMPLE' , 'simple') , ('DOUBLE' , 'double') , ('VIP' , 'vip') , (('SALE' , 'sale')))
class Room(models.Model):
        hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
        room_number = models.CharField()
        price= models.FloatField(blank=True, null=True , default=100) 
        capacity = models.IntegerField()
        total_price = models.FloatField(blank=True, null=True)
        is_available = models.BooleanField(default=False)
        room_type = models.CharField(choices=room_choices_type)

        room_type = models.ForeignKey(
        RoomType,
        related_name="room_type",
        on_delete=models.CASCADE,
    )

        def __str__(self):
            return self.hotel + "---" + self.room_number
