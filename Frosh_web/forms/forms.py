from django import forms
from .models import FormEntry, Preference,WorkshopPass

class FormEntryForm(forms.ModelForm):
    class Meta:
        model = FormEntry
        fields = ('name', 'roll_no', 'phone_no', 'email', 'preferences')


    preferences = forms.ModelMultipleChoiceField(queryset=Preference.objects.all(), widget=forms.CheckboxSelectMultiple)
