from django.contrib import admin
from .models import Webpage,AccessRecord,Topics,UsersModel,UserProfileModel

# Register your models here.
admin.site.register(Topics)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UsersModel)
admin.site.register(UserProfileModel)
