from django.contrib import admin
from testapp.models import parent1,child,parent2
# Register your models here.
admin.site.register(parent1)
admin.site.register(parent2)
admin.site.register(child)
