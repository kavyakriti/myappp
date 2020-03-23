from django.contrib import admin

# Register your models here.
from . import *

admin.site.register(models.Business)
admin.site.register(models.Technical)
''' admin.site.register(models.Departments)
admin.site.register(models.DeptEmp)
admin.site.register(models.DeptManager)
admin.site.register(models.Titles) '''

