from django.contrib import admin
from accounts.models import Client, CustomUser, AdminHOD, Staffs

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Client)
