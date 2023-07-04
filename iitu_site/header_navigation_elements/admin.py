from django.contrib import admin

from .models import NavigationElement, DropdownNavigationElement1, DropdownNavigationElement2, DropdownNavigationElement3

# Register your models here.
admin.site.register(NavigationElement)
admin.site.register(DropdownNavigationElement1)
admin.site.register(DropdownNavigationElement2)
admin.site.register(DropdownNavigationElement3)
