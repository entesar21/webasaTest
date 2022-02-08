from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,OTPRequest,Profile

admin.site.register(OTPRequest)
admin.site.register(Profile)

@admin.register(User)
class AppUserAdmin(UserAdmin):
    pass
