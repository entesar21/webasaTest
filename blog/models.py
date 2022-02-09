from django.db import models
from django_jalali.db import models as jmodels

class Article(models.Model):
    article_title = models.CharField(max_length=250)
    article_body = models.TextField()
    article_alt = models.TextField(default='',blank=True,null=True)
    article_image = models.ImageField(upload_to='store_image/blog_image/', null=True, blank=True)
    created = jmodels.jDateTimeField(auto_now_add=True)



    def save(self, *args, **kwargs):
        self.article_alt = self.article_title
        super().save(*args, **kwargs)  # Call the "real" save() method.



    def __str__(self):
        return self.article_title
