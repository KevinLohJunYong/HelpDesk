from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from User.models import BaseUser

class BaseUserInline(admin.StackedInline):
    model = BaseUser
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (BaseUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
