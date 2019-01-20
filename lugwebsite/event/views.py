from django.shortcuts import render,redirect


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()
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

class EventDetail(LoginRequiredMixin,generic.DetailView):
    model = models.Event

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )
#Experiment with update view

class UpdateEvent(generic.UpdateView,LoginRequiredMixin):
    template_name = 'event/event_form.html'
    success_url = reverse_lazy("event:all")
    form_class = forms.EventForm
    model = models.Event

#Experiment ended here

class DeleteEvent(LoginRequiredMixin, generic.DeleteView):
    model = models.Event
    success_url = reverse_lazy("event:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Event Deleted")
        return super().delete(*args, **kwargs)


class UserEvents(LoginRequiredMixin,generic.ListView):
    model = models.Event
    template_name = "event/user_event_list.html"

    def get_queryset(self):
        try:
            self.event_user = User.objects.prefetch_related("events").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.event_user.events.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_user"] = self.event_user
        return context