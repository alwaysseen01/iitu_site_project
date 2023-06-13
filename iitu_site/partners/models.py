from django.db import models

# Create your models here.
from django.db import models


class Partners(models.Model):
    image = models.ImageField(upload_to='partners_images/')

    class Meta:
        verbose_name_plural = "Partners"
