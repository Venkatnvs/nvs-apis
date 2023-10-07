from django.urls import path
from .views import *

urlpatterns = [
    path("",HomePage,name="frontend_home"),
    path("test/",TestPage,name="frontend_test"),
]
