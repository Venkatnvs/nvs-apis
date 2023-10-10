from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import EndPoints

TokenAdmin.raw_id_fields = ['user']

admin.site.register(EndPoints)