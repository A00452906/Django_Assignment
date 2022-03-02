from django.urls import path
from . import views

urlpatterns= [
   # path("Get_Hotel_list/", views.Get_Hotel_List, name="hotelList"),
   # path("hotel_list/<str:pk>", views.Hotels_detail, name="hotelDetail"),
  #  path("generics_hotel_list/", views.get_generics_list.as_view(), name="genericsList"),
   path("hotel_list/", views.hotel_list)
]