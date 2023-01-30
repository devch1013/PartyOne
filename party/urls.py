from django.urls import path
from .views import *

urlpatterns = [
    path("", PartyBasicView.as_view(), name="party"),
]
