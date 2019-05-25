from django import forms
from .models import  ClientRequest



class ClientRequestForm(forms.ModelForm):

	class Meta:
		model = ClientRequest
		fields=('client_name','phone_no','no_of_people','date_of_booking','time_of_booking','client_email')
	

