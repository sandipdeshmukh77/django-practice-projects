from django.contrib import admin
from testapp.models import Employee,ProxyEmployee2,ProxyEmployee3
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eaddr','esal']

class ProxyEmployee2Admin(admin.ModelAdmin):
    list_display=['id','eno','ename','eaddr','esal']

class ProxyEmployee3Admin(admin.ModelAdmin):
    list_display=['id','eno','ename','eaddr','esal']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee2,ProxyEmployee2Admin)
admin.site.register(ProxyEmployee3,ProxyEmployee3Admin)
