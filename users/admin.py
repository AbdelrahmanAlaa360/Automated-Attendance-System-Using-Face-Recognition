from django.contrib import admin
from .models import User ,ProfileImage,TrainImage
from django.contrib.auth.admin import UserAdmin
admin.site.register(User)
admin.site.register(ProfileImage)
admin.site.register(TrainImage)