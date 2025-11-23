from django.contrib import admin
from .models import Cat, Employee, Volunteer, Application

admin.site.register(Cat)
admin.site.register(Employee)
admin.site.register(Volunteer)
admin.site.register(Application)