from django.db import models
from users.models import User
from course.models import Course

from django.db.models import F, Sum, Max

def total_price(self):
    return self.objects.aggregate(Sum('product__course_discounted_price'))

class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    product = models.ManyToManyField(Course, related_name='product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.BigIntegerField(default=1, null=True, blank=True)
    class Meta:
        ordering = ['cart_id', '-created_at']


    def __str__(self):
        return f'{self.cart_id}'

    def save(self, *args, **kwargs):
        self.total_price = self.product.aggregate(sum = Sum('course_discounted_price'))['sum']
        super().save(*args, **kwargs)
