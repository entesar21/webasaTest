from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=250)
    article_body = models.TextField()
    article_alt = models.TextField(default='')
    article_image = models.ImageField(upload_to='store_image/blog_image/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)



    def save(self, *args, **kwargs):
        self.article_alt = self.article_title
        super().save(*args, **kwargs)  # Call the "real" save() method.



    def __str__(self):
        return self.article_title
