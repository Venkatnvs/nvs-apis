from django.urls import path
from .views import *

urlpatterns = [
    path("",HomePage,name="frontend_home"),
    path("<slug>",EndPointView,name="frontend_endpoint"), 
    path("test/",TestPage,name="frontend_test"),
]
