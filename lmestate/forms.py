from django.forms import ModelForm, FileField
from django import forms
from .models import *
from django.views.generic import FormView


class PropertyForm(ModelForm):
    # image = forms.ImageField(widget=FileField(attrs={"multiple": True}))
    class Meta:
        model = Property
        fields = ['property_location', 'price', 'description', 'status', 'image']

    def form_valid(self, form):
        form.instance.agency = self.request.user
        return super().form_valid(form)


class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = ['email', 'description', 'quote']


class AddressForm(ModelForm):
    class Meta:
        model=Address
        fields=['address_line1', 'address_line2', 'city', 'popular_landmark']


class CreateAgency(ModelForm):
    class Meta:
        model=Agency
        fields=['agency_name', 'phone', 'agency_image']

class PropertyImageUploadForm(ModelForm):
    class Meta:
        model = ImageModel
        fields=['image']