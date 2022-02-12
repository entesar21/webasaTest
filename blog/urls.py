from django.urls import path
from .views import *

urlpatterns = [
    path('show_article/', ShowArticle.as_view()),
    path('add_article/', AddArticle.as_view()),
    path('comments/<int:pk>', CommentRelatedToArticle.as_view()),
    path('comments/<int:pk>/vote', VoteCreate.as_view()),
]
