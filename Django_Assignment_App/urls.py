from django.urls import path
from . import views

urlpatterns= [
   path("hotel_list/", views.hotel_list)
]
