from django.db import models

# Create your models here.
from django.db import models


class MainNews(models.Model):
    image = models.ImageField(upload_to='news_images/')
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Main news"


class News(models.Model):
    image = models.ImageField(upload_to='news_images/')
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
