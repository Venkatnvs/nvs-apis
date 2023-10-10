from django.urls import path
from .views import *

urlpatterns = [
    path('states/', states_pin.as_view(), name='home'),
    path('zip/', ZipCode.as_view(), name='home-zip'),
    path('d/', HomeTest, name='hometest'),
    path('statejs/v1/<token>/user.js', ServerJavascript, name='hometestserve')
]