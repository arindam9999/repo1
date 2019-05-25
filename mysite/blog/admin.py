from django.contrib import admin
from .models import Hotel , City ,ClientRequest , HotelImage,CityImage


admin.site.register(Hotel)
admin.site.register(City)
admin.site.register(ClientRequest)
admin.site.register(HotelImage)
admin.site.register(CityImage)
