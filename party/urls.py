from django.urls import path
from .views import *

urlpatterns = [
    path("", PartyBasicView.as_view(), name="party"),
    path("/<str:col>", PartyDetailView.as_view(), name="party_detail"),
]
