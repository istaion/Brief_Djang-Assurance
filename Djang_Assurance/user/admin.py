from django.contrib import admin
from .models import CustomUser, StaffUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(StaffUser)