from django.urls import path
from .views import *

urlpatterns = [
    path('show_footer/', ShowFooter.as_view()),
    path('edit_footer/', EditFooter.as_view()),
    path('add_footer/', AddFooter.as_view()),
]
