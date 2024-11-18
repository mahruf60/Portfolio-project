from django.contrib import admin

from main_app.models import *
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ContactInfo)
admin.site.register(Resume)