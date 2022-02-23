from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns = [
    path('users',userView.as_view())
]
