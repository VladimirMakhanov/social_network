from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from social_network.models import User

admin.site.register(User, UserAdmin)

