from django import forms
from .models import  ClientRequest ,ClientBookingRequest, ClientRegistrationRequest



class ClientRequestForm(forms.ModelForm):

	class Meta:
		model = ClientRequest
		fields=('client_name','phone_no','no_of_people','date_of_booking','time_of_booking','client_email')


class ClientBookingRequestForm(forms.ModelForm):

	class Meta:
		model = ClientBookingRequest
		fields=('client_name','phone_no','no_of_people','date_of_booking','theme','client_email')
	

class ClientRegistrationRequestForm(forms.ModelForm):

	class Meta:
		model = ClientRegistrationRequest
		fields=('venue_name','phone_no','city_name')
	

