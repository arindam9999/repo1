from django.db import models

class City(models.Model):
	name=models.CharField(max_length=100)
	#image=models.ImageField(default='default.bmp',upload_to='city_pics')


	def __str__(self):
		return self.name



class Hotel(models.Model):
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=200)
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	facility=models.TextField(default='none')
	price_per_person=models.TextField(default='none')

	def __str__(self):
		return self.name

class ClientRequest(models.Model):
	client_name= models.CharField(max_length=100)
	phone_no=models.CharField(max_length=15)
	no_of_people=models.CharField(max_length=3)
	hotel_name=models.ForeignKey(Hotel,on_delete=models.CASCADE)
	date_of_booking=models.DateField()
	time_of_booking=models.TimeField()
	client_email=models.EmailField()
	def __str__(self):
		return self.client_name

class CityImage(models.Model):
	name=models.ForeignKey(City,on_delete=models.CASCADE)
	image=models.ImageField(default='default.bmp',upload_to='city_pics')

class HotelImage(models.Model):
	name=models.ForeignKey(Hotel,on_delete=models.CASCADE)
	image=models.ImageField(default='default.bmp',upload_to='hotel_pics')



