from django.db import models


# Create your models here.
class ContactsElement(models.Model):
    icon = models.ImageField(upload_to='footer_contacts_icons/')
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Contacts' elements"

    def __str__(self):
        return self.title
