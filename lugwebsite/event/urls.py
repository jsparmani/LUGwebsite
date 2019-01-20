from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
				
				path('new/',views.CreateEvent.as_view(),name = 'create'),
]