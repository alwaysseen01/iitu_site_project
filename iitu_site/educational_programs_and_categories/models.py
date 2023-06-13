from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class EducationalProgram(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='programs_icons/')
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    faculties_count = models.IntegerField()

    class Meta:
        verbose_name_plural = "Educational programs"

    def __str__(self):
        return self.title
