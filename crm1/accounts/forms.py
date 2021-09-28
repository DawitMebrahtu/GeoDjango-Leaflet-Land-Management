from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import *
from django.contrib.auth.models import User



		
class CreateUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2'] 


class TransferForm(forms.ModelForm):
	class Meta:
		model = transfer_request
		fields = ['reciever', 'poly']

		exclude = ['date_created','sender',]
		
#	def __init__(self,sender=sender,**kwargs):
#		super(TransferForm,self).__init__(*args,**kwargs)
#		self.fields['poly'].queryset= poly.objects.filter(owner = sender)
#		print('herecomes',self.instance)

class GrantForm(forms.ModelForm):

	class Meta:
		model = grant_land
		fields = ['grant_reciever', 'grant_poly']
	#Filter the land ('grant_poly') object to only get lands without owners
	def __init__(self,*args,**kwargs):
		super(GrantForm,self).__init__(*args,**kwargs)
		self.fields['grant_poly'].queryset=poly.objects.filter(owner_id__isnull=True)

	#	exclude = ['date_created',]








		#exclude = ('date_created',)

	#def __init__(self, user=None, **kwargs):
	#	super(TransferForm, self).__init__(**kwargs)
	#	if user:
	#		self.fields['poly'].queryset = models.poly.objects.filter(user=user)
