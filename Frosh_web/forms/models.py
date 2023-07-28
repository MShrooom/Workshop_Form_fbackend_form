# myapp/models.py
from django.db import models

class Preference(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class WorkshopPass(models.Model):
    form_entry = models.ForeignKey('FormEntry', on_delete=models.CASCADE, null=True, blank=True)
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE, null=True, blank=True)
    total_passes = models.IntegerField(default=0)
    allocated_passes = models.IntegerField(default=0)

class FormEntry(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    preferences = models.ManyToManyField(Preference)
