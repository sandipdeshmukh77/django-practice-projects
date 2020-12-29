from django.contrib import admin
from testapp.models import FilterClass
# Register your models here.
class FilterClassAdmin(admin.ModelAdmin):
    list_display=['name','addr','subject','dept','date']

admin.site.register(FilterClass,FilterClassAdmin)    
