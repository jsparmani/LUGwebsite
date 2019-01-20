from django.urls import path, re_path
from . import views

app_name = 'event'

urlpatterns = [
				
				path('',views.EventList.as_view(),name='all'),
				path('new/',views.CreateEvent.as_view(),name = 'create'),
				re_path(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.EventDetail.as_view(),name="single"),
				re_path(r"by/(?P<username>[-\w]+)/$",views.UserEvents.as_view(),name="for_user"),
				re_path(r"delete/(?P<pk>\d+)/$",views.DeleteEvent.as_view(),name="delete"),


]