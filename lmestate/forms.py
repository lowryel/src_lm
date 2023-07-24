from django.forms import ModelForm, FileField
from django import forms
from .models import *
from django.views.generic import FormView


class PropertyForm(ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Property
        fields = ['property_location', 'price', 'description', 'status', 'image']

    def form_valid(self, form):
        form.instance.agency = self.request.user
        return super().form_valid(form)


