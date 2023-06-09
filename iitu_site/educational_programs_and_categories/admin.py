from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EducationalProgram, Category

admin.site.register(EducationalProgram)
admin.site.register(Category)
