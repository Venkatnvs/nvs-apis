from django.urls import path
from .views import *

urlpatterns = [
    path("",HomePage,name="apifrontend_home"),
    path("d/<slug>",EndPointView,name="apifrontend_endpoint"), 
    path("test/",TestPage,name="apifrontend_test"),
]
