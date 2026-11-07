from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra info', {'fields': ('phone', 'address', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra info', {'fields': ('email', 'first_name', 'last_name', 'phone')}),
    )
    list_display = ('username', 'email', 'full_name', 'phone', 'is_staff')


admin.site.register(User, CustomUserAdmin)