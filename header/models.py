from django.db import models
from datetime import datetime


class Menu(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self',null=True,blank=True,related_name='children',on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Logo(models.Model):
    logo_text = models.CharField(max_length=120)
    logo_alt = models.TextField(default='')
    logo_image = models.ImageField(upload_to='store_image/logo_image/',null=True, blank=True)


    def save(self, *args, **kwargs):
        self.logo_alt = self.logo_text
        super().save(*args, **kwargs)  # Call the "real" save() method.



    def __str__(self):
        return self.logo_text

