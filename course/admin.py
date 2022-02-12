from django.contrib import admin

from .models import *


admin.site.register(Course)
admin.site.register(CourseCategory)

admin.site.register(Vote)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'created', 'active',)
    list_filter = ('active', 'created')
    # list_editable = ('active',)