from django.db import models


# Create your models here.


class Hotel(models.Model):
    Hotel_id = models.IntegerField(primary_key=True)
    Hotel_name = models.CharField(max_length=200, null=False)
    Hotel_price = models.IntegerField()
    Hotel_rating = models.IntegerField()
    Hotel_location=models.CharField(max_length=500,null=False)

    def __str__(self):
        return self.Hotel_name