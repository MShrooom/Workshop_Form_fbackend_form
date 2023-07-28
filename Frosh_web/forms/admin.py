from django.contrib import admin
from .models import FormEntry, Preference,WorkshopPass

admin.site.register(FormEntry)
admin.site.register(Preference)
admin.site.register(WorkshopPass)