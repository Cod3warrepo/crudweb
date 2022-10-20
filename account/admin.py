from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

class CustomAdmin(UserAdmin):
    list_display = ('email', 'username', 'dob', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'hide_email')
    search_fields = ('email', 'username')
    readonly_fields = ('date_join', 'last_login')


    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(CustomUserModel, CustomAdmin)