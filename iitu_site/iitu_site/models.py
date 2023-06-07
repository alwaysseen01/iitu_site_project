from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='news/')
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    content = models.TextField()
