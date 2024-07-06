from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .models import CustomUser

# This code should only be in one place
# try:
#     admin.site.register(CustomUser, UserAdmin)
# except admin.sites.AlreadyRegistered:
#     pass

class UserModel(UserAdmin):
    ordering = ('email',)


admin.site.register(CustomUser, UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Session)
