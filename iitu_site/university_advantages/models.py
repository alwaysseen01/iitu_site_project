from django.db import models


# Create your models here.
class UniversityAdvantage(models.Model):
    icon = models.ImageField(upload_to='advantages_icons/')
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name_plural = "University advantages"

    def __str__(self):
        return self.title
