from django.urls import path
from .views import testserver

urlpatterns = [
    path("", testserver, name="testserver"),
]
