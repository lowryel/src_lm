from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Address)
admin.site.register(Agency)
admin.site.register(Property)

