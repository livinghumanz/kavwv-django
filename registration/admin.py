from django.contrib import admin
from .models import Coursereg, Selfupload
# Register your models here.
admin.site.register([Coursereg,Selfupload])