from django.shortcuts import render
from django.core.mail import send_mail
from . import models
# Create your views here.

def sendEmail(request):
	email_dict = models.Receiver.objects.all().values('email')
	email_list = [u['email'] for u in email_dict]
	send_mail("LUG, Pending Event Verification Request",'A new event is registered for advertisement. Please have a look at it and verify it as soon as possible','lug.tiet@yahoo.com',email_list,fail_silently = False)
	return render(request,'emails/email_sent.html')