from django.db import models

# Create your models here.
from django.db import models


class FooterElementCategory(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories of footer elements"

    def __str__(self):
        return self.title


class FooterElement(models.Model):
    category = models.ForeignKey(FooterElementCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Footer elements"

    def __str__(self):
        return self.title
