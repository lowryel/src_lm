from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("agent/list/<int:pk>/", agentList, name="agent-list"),
    path("agent/<str:property_id>/", estate_detail, name="estate-detail"),
    path("base/", base, name="base"),
]
