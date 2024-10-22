from django.db import models


class Hotel(models.Model):
        name = models.CharField(max_length=100)
        adress = models.CharField(max_length=100)
        description = models.CharField(max_length=50)
        phone_number = models.CharField(max_length=50)
        email = models.EmailField()
        notation = models.FloatField(default=1)

        def __str__(self):
            return self.name + "---" + self.notation

