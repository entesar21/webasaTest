from django.db import models
from datetime import datetime

# Create your models here.

class Footer(models.Model):
    footer_about_us= models.TextField(default='default about us')
    footer_telegram = models.CharField(max_length=120,default='http://telegram.me/webasa')
    footer_insta = models.CharField(max_length=120,default='http://insta.me/webasa')
    footer_whats_app = models.CharField(max_length=120,default='http://whatsapp.me/webasa')
    footer_phone = models.IntegerField(default='02598653269')
    created_at = models.DateTimeField(default=datetime.now)


