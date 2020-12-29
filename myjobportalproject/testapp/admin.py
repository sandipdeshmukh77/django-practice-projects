from django.contrib import admin
from testapp.models import punejobs,hydjobs,chennaijobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','title','eligibility','address','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['id','date','company','title','eligibility','address','email','phonenumber']

admin.site.register(punejobs,punejobsAdmin)
admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
