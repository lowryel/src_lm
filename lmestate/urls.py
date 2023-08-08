from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("agent/list/<int:pk>/", agentList, name="agent-list"),
    path("agent/<str:property_id>/", estate_detail, name="estate-detail"),
    path("base/", base, name="base"),
    path("address/", address, name="address"),
    path("agencycreate/", agencycreate, name="create-agency"),
    path("property_images_add/<int:id>/", property_images_add, name="add-properties"),
]
