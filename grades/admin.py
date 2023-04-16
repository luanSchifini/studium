from django.contrib import admin

from .models import Student
admin.site.register(Student)

from .models import Assignment
admin.site.register(Assignment)

# Register your models here.
