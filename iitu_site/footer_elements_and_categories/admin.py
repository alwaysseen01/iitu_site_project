from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FooterElement, FooterElementCategory

admin.site.register(FooterElement)
admin.site.register(FooterElementCategory)
