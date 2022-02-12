from django.contrib import admin
from blog.models import Article, Comment, Vote


admin.site.register(Article)
admin.site.register(Vote)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'created', 'active',)
    list_filter = ('active', 'created')
    # list_editable = ('active',)