from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib import auth
from accounts.models import User
class UserCreateForm(UserCreationForm):

	class Meta():
		fields = ('first_name','last_name','username','email','password1','password2')
		model = User

		def __init__(self,*args,**kwargs):
			super.__init__(*args,**kwargs)
			self.fields['username'].label='Username'
			self.fields['first_name'].label='First Name'
			self.fields['last_name'].label='Last Name'
			self.fields['email'].label='Email Address'
			

