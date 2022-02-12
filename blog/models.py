from django.db import models
from django_jalali.db import models as jmodels
from users.models import User

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


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_article_comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "comment by {} on article {}".format(self.name,self.article)

    # def children(self):
    #     return Comment.objects.filter(parent=self)

    # @property
    # def is_parent(self):
    #     if self.parent is not None:
    #         return False
    #     return True


class Vote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_vote')

    def __str__(self):
        return self.voter.username + ' voted on ' + self.comment.article.article_title