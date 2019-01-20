from django.shortcuts import render


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

# Create your views here.

# VIEWS RELATED TO POST CREATE, LIST, DELETE, DETAIL, USER LIST
# class CreateEvent(LoginRequiredMixin, generic.CreateView):
#     model = models.Event
#     fields = [  'organization_name',
#     			'organization_logo',
#     			'title',
#     			'description',
# 				'start_date',
# 				'end_date',
# 				'start_time',
# 				'end_time',
# 				'venue',
# 				'link',
# 				'price',
# 				'event_image_1',
# 				'event_image_2',
# 				'event_image_3',
# 				'event_image_4',
# 				'contact_no',
# 				'contact_email',
# 			]


#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return super().form_valid(form)


class CreateEvent(LoginRequiredMixin, generic.FormView):
    template_name = 'event/event_form.html'
    form_class = forms.EventForm
    success_url = reverse_lazy('event:all')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class EventList(generic.ListView):
    model = models.Event
    ####