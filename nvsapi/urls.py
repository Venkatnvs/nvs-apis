from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api1.urls")),
    path('', include("frontend.urls")),
]
