__author__ = "Trevor Munroe"

# pages/urls.py
from django.urls import path
from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home"),
]