from django.contrib import admin

# Register your models here.
from . import *

admin.site.register(models.User)
admin.site.register(models.News)

