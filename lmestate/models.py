from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.signals import post_save, pre_save
import uuid


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
            agent=request.user
            return self.get_queryset().get(agent=agent)
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

def agency_property_count(sender, instance, created=True, *args, **kwargs):
    print("pre_save property count")

post_save.connect(agency_property_count, sender=Agency)


# class ImageModel(models.Model):
#     file = models.ImageField(upload_to='img')

#     def __str__(self) -> str:
#         return self.file.url


PROPERTY_CHOICES = (("For Sale", "For Sale"),("Rent", "Rent"))

class Property(models.Model):
    property_id = models.UUIDField(default=uuid.uuid4, unique=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)
    property_location = models.CharField(max_length=512, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img")
    status = models.CharField(choices=PROPERTY_CHOICES, max_length=64, default="For Sale")

    class Meta:
        verbose_name="Property"
        verbose_name_plural = "Properties"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

def agency_property_count(sender, instance, *args, **kwargs):
    print("pre_save property count 2")
    total_property=0
    agent=instance.id
    agency_property = Property.objects.filter(agency=agent)
    for item in agency_property:
        total_property +=1
    instance.property_count=total_property
    print(instance.property_count)
    item.save()
    return instance.property_count

pre_save.connect(agency_property_count, sender=Agency)
