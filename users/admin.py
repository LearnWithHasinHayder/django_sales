from django.contrib import admin
from .models import Profile, UserOTP
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserOTPInline(admin.StackedInline):
    model = UserOTP
    can_delete = False
    verbose_name_plural = 'User OTP'

class UserAdmin(BaseUserAdmin):
    # inlines = [ProfileInline, UserOTPInline]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
