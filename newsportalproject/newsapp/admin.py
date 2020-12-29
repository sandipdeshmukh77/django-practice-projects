from django.contrib import admin
from newsapp.models import student
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['name','marks']
admin.site.register(student,studentadmin)
