from django.db import models


# Create your models here.
class FooterSocialNetwork(models.Model):
    icon = models.ImageField(upload_to='footer_social_networks_icons/')

    class Meta:
        verbose_name_plural = "Social network icon"
