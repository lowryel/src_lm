from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Address)

class EnquiryModelAdmin(admin.ModelAdmin):
    list_display = ["email", "quote", "time"]
admin.site.register(Enquiry, EnquiryModelAdmin)
admin.site.register(ImageModel)

class AgencyModelAdmin(admin.ModelAdmin):
    list_display = ["agency_name", "agent_location", "phone", "date_registered"]
    list_editable = ["phone"]
admin.site.register(Agency, AgencyModelAdmin)


class PropertyAdmin(admin.ModelAdmin):
    def agency_name(self, obj):
        return obj.agency.agency_name
    
    list_display = ["agency_name", "property_location", "price", "date_posted", "status"]
    list_per_page = 10
    list_max_show_all=10
    list_filter=["status", "property_location"]
admin.site.register(Property, PropertyAdmin)
admin.site.site_header = "LM Estate Administration"
admin.site.site_url = "http://127.0.0.1:8000"
admin.site.site_title="LM Estate Administration"