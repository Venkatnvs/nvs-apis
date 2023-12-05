from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name','last_name', 'is_active', 'is_staff', 'is_completed']
    search_fields = ['email', 'first_name','last_name']
    list_filter = ['is_active', 'is_staff', 'is_completed','is_socialaccount']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name','last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_socialaccount', 'is_completed')}),
        ('Important dates', {'fields': ('last_login', 'date_joined','created_at','last_updated')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )

    ordering = ['email']
    readonly_fields = ('created_at', 'last_updated')

admin.site.register(CustomUser, CustomUserAdmin)
