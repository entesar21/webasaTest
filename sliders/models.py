
from django.db import models

# Create your models here.

class Slider(models.Model):
    slider_title = models.CharField(max_length=120)
    slider_alt = models.TextField(default='')
    slider_image = models.ImageField(upload_to='store_image/sliders_image/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def save(self, *args, **kwargs):
        self.slider_alt = self.slider_title + ' متن تست '
        super().save(*args, **kwargs)  # Call the "real" save() method.



    def __str__(self):
        return self.slider_title
