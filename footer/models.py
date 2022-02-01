from django.db import models
from datetime import datetime

# Create your models here.

class Footer(models.Model):
    footer_about_us= models.TextField(default='default about us',blank=True,null=True)
    footer_telegram = models.CharField(max_length=120,default='http://www.telegram.me/webasa',blank=True,null=True)
    footer_insta = models.CharField(max_length=120,default='https://www.instagram.com/webasa',blank=True,null=True)
    footer_whats_app = models.CharField(max_length=120,default='http://www.whatsapp.me/webasa',blank=True,null=True)
    footer_aparat = models.CharField(max_length=120,default='https://www.aparat.com/webasa',blank=True,null=True)
    footer_youtube = models.CharField(max_length=120,default='https://www.youtube.com/webasa',blank=True,null=True)
    footer_twitter = models.CharField(max_length=120,default='https://twitter.com/webasa',blank=True,null=True)
    footer_linkedin = models.CharField(max_length=120,default='https://www.aparat.com/webasa',blank=True,null=True)
    footer_facebook = models.CharField(max_length=120,default='https://www.facebook.com/webasa',blank=True,null=True)
    footer_phone = models.IntegerField(default='02598653269',blank=True,null=True)
    footer_address = models.IntegerField(default='02598653269',blank=True,null=True)
    created_at = models.DateTimeField(default=datetime.now)


