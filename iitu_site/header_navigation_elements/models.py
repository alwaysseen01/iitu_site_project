from django.db import models


# Create your models here.
class NavigationElement(models.Model):
    title = models.CharField(max_length=255)
    is_dropdown = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Navigation elements"

    def __str__(self):
        return self.title


class DropdownNavigationElement1(models.Model):
    title = models.CharField(max_length=255)
    parent_navigation_element = models.ForeignKey(NavigationElement, on_delete=models.CASCADE)
    is_dropdown = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Dropdown(1st panel) navigation elements"

    def __str__(self):
        return self.title


class DropdownNavigationElement2(models.Model):
    title = models.CharField(max_length=255)
    parent_dropdown_navigation_element = models.ForeignKey(DropdownNavigationElement1, on_delete=models.CASCADE)
    is_dropdown = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Dropdown(2nd panel) navigation elements"

    def __str__(self):
        return self.title


class DropdownNavigationElement3(models.Model):
    title = models.CharField(max_length=255)
    parent_dropdown_navigation_element = models.ForeignKey(DropdownNavigationElement2, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Dropdown(3rd panel) navigation elements"

    def __str__(self):
        return self.title
