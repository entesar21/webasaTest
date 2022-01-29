from django.urls import path
from .views import *

urlpatterns = [
    path('show_course/', ShowCourse.as_view()),
    path('add_course/', AddCourse.as_view()),
]
