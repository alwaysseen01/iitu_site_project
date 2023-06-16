from django.db import models


# Create your models here.
class NavigationElement(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Navigation elements"

    def __str__(self):
        return self.title
