from django.contrib import admin
from testapp.models import movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['name','actor','actress','rdate','rating']

admin.site.register(movie,MovieAdmin)
