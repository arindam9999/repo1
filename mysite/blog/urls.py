from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
	path('about/', views.about,name='blog-about'),
	path('city/<int:pk>/',views.city_detail,name='city-detail'),
	path('hotel/<int:pk>/',views.hotel_detail,name='hotel-detail'),
	path('form1/',views.form1,name='form1'),
	path('form2/',views.form2,name='form2'),
    
]
