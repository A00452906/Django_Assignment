from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .Serializers import HotelSerializers
from rest_framework import generics
from rest_framework import filters
from .models import Hotel

@api_view(['GET','POST'])
def hotel_list(request):
    if request.method == "GET":
        hotels_list = Hotel.objects.all()
        hotel_serializer = HotelSerializers(hotels_list, many=True)
        print(hotel_serializer.data)
        return Response(hotel_serializer.data)
    if request.method == 'POST':
        hotel_data = request.data
        serialize_hotel_data = HotelSerializers(data=hotel_data)
        if serialize_hotel_data.is_valid():
            serialize_hotel_data.save()
        return Response({"Message": "Hotel details added Successfully"})

from django.shortcuts import render

# Create your views here.
