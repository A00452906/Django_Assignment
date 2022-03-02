from rest_framework import serializers
from .models import Hotel


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['Hotel_id','Hotel_name', 'Hotel_price','Hotel_rating','Hotel_location']