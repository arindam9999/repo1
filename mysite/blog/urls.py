from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
	path('about/', views.about,name='blog-about'),
	path('city/<int:pk>/',views.city_detail,name='city-detail'),
	path('hotel/<int:pk>/',views.hotel_detail,name='hotel-detail'),
    
]
