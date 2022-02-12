import uuid
import random
import string
import datetime
from datetime import timedelta
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
from users.sender import send_otp

from django.db.models.signals import post_save

from django_jalali.db import models as jmodels

class User(AbstractUser):
    pass
#8
class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self,receiver,request,password):
        current_time=timezone.now()
        return self.filter(
            receiver=receiver,
            request_id=request,
            password=password,
            created__lt=current_time,
            created__gt=current_time-timedelta(seconds=120)
        ).exists()

#3 third this one
class OTPManager(models.Manager):

#7
    def get_queryset(self):
        return OtpRequestQuerySet(self.model,self._db)

#6
    def is_valid(self, receiver, request, password):
        return self.get_queryset().is_valid(receiver,request,password)

#4 fourth this one
    def generate(self, data):
        otp = self.model(channel=data['channel'], receiver=data['receiver'])
        otp.save(using=self._db)
        send_otp(otp)
        return otp

#2 second this
def generate_otp():
    rand=random.SystemRandom()
    digits=rand.choices(string.digits,k=4)
    return ''.join(digits)

#1 first this one
class OTPRequest(models.Model):
    class OtpChannel(models.TextChoices):
        PHONE = 'Phone'
        EMAIL = 'E_Mail'
    request_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    channel = models.CharField(max_length=10,choices=OtpChannel.choices,default=OtpChannel.PHONE)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4,default=generate_otp)
    created = models.DateTimeField(auto_now_add=True,editable=False)
#5 fifth
    objects=OTPManager()

#------------------------------------PROFILE---------------------------------------------#


class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'

    profile_image = models.ImageField(upload_to='store_image/profile_image', null=True, blank=True)
    code_melli = models.CharField(max_length=10,default='1234567890')
    gender = models.CharField(max_length=10,choices=Gender.choices,default=Gender.MALE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(default="جایی برای معرفی خودتان...",null=True,blank=True)
    registration_date = jmodels.jDateTimeField(auto_now_add=True)



    def __str__(self):
        return self.user.first_name+' '+self.user.last_name+' '+self.user.username

def save_profile_user(sender, **kwargs):
    print(kwargs)
    if kwargs['created']:
        profile_user = Profile.objects.create(user=kwargs['instance'])
        print(profile_user)
        profile_user.save()

post_save.connect(save_profile_user, sender=User)

