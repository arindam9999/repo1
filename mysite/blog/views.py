from django.shortcuts import render, get_object_or_404
from .models import Hotel , City , GalleryPic , Profile , HotelImage , ClientBookingRequest , ClientRegistrationRequest
from django.shortcuts import redirect
from .forms import ClientRequestForm 
from django.contrib import messages
from django.http import HttpResponse


def home(request):
	cities=City.objects.all()
	pics=GalleryPic.objects.all()
	profiles=Profile.objects.all()
	title= "Home"
	return render(request,'blog/home.html',{'cities':cities ,'pics':pics ,'profiles':profiles,'title':title})


def about(request):
	title="About Us"
	profiles=Profile.objects.all()
	return render(request,'blog/about.html',{'title':title , 'profiles':profiles})


def city_detail(request,pk):
	city=get_object_or_404(City,pk=pk)
	hotels=Hotel.objects.filter(city_id=city.id)
	title= city.name
	return render(request,'blog/city.html',{'city':city , 'hotels':hotels, 'title':title})
	
def hotel_detail(request,pk):
	hotel=get_object_or_404(Hotel,pk=pk)
	hotel_images=HotelImage.objects.filter(name_id=hotel.id)
	if request.method=='POST':
		form= ClientRequestForm (request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.hotel_name = hotel
			post.save()
			username=form.cleaned_data.get('client_name')
			messages.success(request,f' {username},we thank u for applying to us! Your request has been successfully generated.' )
			return redirect('blog-home')

	else :
		form= ClientRequestForm ()
	return render(request,'blog/hotel.html',{ 'hotel':hotel, 'form':form, 'hotel_images':hotel_images})


def form1(request):
	title="Book an event"
	if request.method=='POST':
		aclient_name = request.POST.get('client_name')
		aphone_no=request.POST.get('phone_no')
		ano_of_people=request.POST.get('no_of_people')
		adate_of_booking=request.POST.get('date_of_booking')
		atheme=request.POST.get('theme')
		aclient_email=request.POST.get('theme')
		if aclient_email and aclient_name and aphone_no:
			ClientBookingRequest.objects.create(client_name=aclient_name, phone_no=aphone_no, no_of_people=ano_of_people , date_of_booking=adate_of_booking , theme=atheme, client_email=aclient_email  )
			messages.success(request,f' {aclient_name},we thank u for applying to us! Your request has been successfully generated.' )
			return redirect('blog-home')
			
	return render(request,'blog/form1.html',{  'title':title})



def form2(request):
	title="Register your Venue"
	if request.method=='POST':
		avenue_name = request.POST.get('avenue_name')
		aphone_no=request.POST.get('aphone_no')
		acity_name=request.POST.get('acity_name')
		if acity_name and avenue_name and aphone_no:
			ClientRegistrationRequest.objects.create(venue_name=avenue_name, phone_no=aphone_no , city_name=acity_name )
			messages.success(request,f' {avenue_name},we thank u for applying to us! Your request has been successfully generated.' )
			return redirect('blog-home')
			
	return render(request,'blog/form2.html',{  'title':title})

	

