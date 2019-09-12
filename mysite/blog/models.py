from django.db import models

class City(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(default='default.bmp',upload_to='city_pics')


	def __str__(self):
		return self.name



class Hotel(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(default='default.bmp',upload_to='hotel_pics')
	location=models.CharField(max_length=200)
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	facility=models.TextField(default='none')

	price_per_person=models.TextField(default='none')
	veg_nonveg_key=models.CharField(max_length=1,default='none')
	nonveg_price=models.CharField(max_length=100,default='none')
	veg_price=models.CharField(max_length=100,default='none')
	nonveg_description=models.TextField(default='none')
	veg_description=models.TextField(default='none')

	

	def __str__(self):
		return self.name

class ClientRequest(models.Model):
	client_name= models.CharField(max_length=100)
	phone_no=models.CharField(max_length=15)
	no_of_people=models.CharField(max_length=3,)
	hotel_name=models.ForeignKey(Hotel,on_delete=models.CASCADE)
	date_of_booking=models.CharField(max_length=100)
	time_of_booking=models.CharField(max_length=100,default='none')
	client_email=models.EmailField()

	def __str__(self):
		return self.client_name

class CityImage(models.Model):
	name=models.ForeignKey(City,on_delete=models.CASCADE)
	image=models.ImageField(default='default.bmp',upload_to='city_pics')

class HotelImage(models.Model):
	name=models.ForeignKey(Hotel,on_delete=models.CASCADE)
	image=models.ImageField(default='default.bmp',upload_to='hotel_pics')


class GalleryPic(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(default='default.bmp',upload_to='gallery_pics')


	def __str__(self):
		return self.name


class Profile(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(default='default.bmp',upload_to='profile_pics')
	description=models.TextField()
	phone_no=models.CharField(max_length=100)


	def __str__(self):
		return self.name


class ClientBookingRequest(models.Model):
	client_name= models.CharField(max_length=100,default='none')
	phone_no=models.CharField(max_length=15,default='none')
	no_of_people=models.CharField(max_length=3,default='none')
	date_of_booking=models.CharField(max_length=100,default='none')
	theme=models.CharField(max_length=100,default='none')
	client_email=models.EmailField()

	def __str__(self):
		return self.client_name



class ClientRegistrationRequest(models.Model):
	venue_name= models.CharField(max_length=100)
	phone_no=models.CharField(max_length=15)
	city_name=models.CharField(max_length=100)

	def __str__(self):
		return self.venue_name




