from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.signals import post_save, pre_save
import uuid

from .multi_file_upload import handle_uploaded_file

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    popular_landmark = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address"

    def __str__(self):
        return self.address_line1


class AgencyManager(models.Manager):
    def get_agency(self, request):
        if request.user.is_authenticated:
            user = request.user
            request.session = user
            return self.get_queryset().get(agent=request.session)
        pass


class Agency(models.Model):
    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=120, null=True)
    agent_location = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True)
    property_count = models.IntegerField(default=0)
    agency_image = models.ImageField(upload_to="img")
    date_registered = models.DateTimeField(auto_now_add=True)

    objects = AgencyManager()

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agency"

    def __str__(self):
        return self.agency_name

    # def get_absolute_url(self):
    #     return self.

# def agency_property_count(sender, instance, *args, **kwargs):
#     if instance.id:
#         instance.save()
#     print("pre_save property count")
#     # instance.save()
#     total=instance.property_set.count()
#     print(total)
#     instance.property_count=total
#     return instance.property_count
# pre_save.connect(agency_property_count, sender=Agency)



PROPERTY_CHOICES = (("For Sale", "For Sale"),("Rent", "Rent"))
class Property(models.Model):
    property_id = models.UUIDField(default=uuid.uuid4, unique=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)
    property_location = models.CharField(max_length=512, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img")
    status = models.CharField(choices=PROPERTY_CHOICES, max_length=64, default="For Sale")

    class Meta:
        verbose_name="Property"
        verbose_name_plural = "Properties"

    # def get_description(self):
    #     return self.description.split("\n")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def agency_property_enquiry(self): # returning properties that enquiry was made for
        return self.enquiry_set.all()
    
    def __int__(self):
        return self.id


def agency_property_count(sender, instance, *args, **kwargs):
    print("pre_save property count 2")
    # count = instance.objects.count()
    # instance.property_count=count
    # return instance.property_count
pre_save.connect(agency_property_count, sender=Agency)



class ImageModel(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img")

    # def __str__(self) -> str:
    #     return self.image.url


class Enquiry(models.Model):
    # A model for potential clients to enquire about a property
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    email = models.EmailField(help_text="Enter a valid email")
    description = models.TextField()
    quote = models.IntegerField(help_text="Quote a figure")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiry"

