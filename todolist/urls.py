
from django.urls import path ,include
from .views import home , contact

urlpatterns = [
    path('',home),
    path('contact/', contact)
]
