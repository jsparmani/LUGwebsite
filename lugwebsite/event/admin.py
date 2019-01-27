from django.contrib import admin
from . import models
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'created_at','verified',]
    list_filter=['verified']


admin.site.register(models.Event, EventAdmin)