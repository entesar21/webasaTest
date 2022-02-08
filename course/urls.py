from django.urls import path
from .views import *

urlpatterns = [
    path('show_course/', ShowCourse.as_view()),
    path('add_course/', AddCourse.as_view()),
    path('number_of_courses/', NumberOfCourses.as_view()),
    path('sum_course_duration/', SumCourseDuration.as_view()),
    path('show_course_category/', ShowCourseCategory.as_view()),
]
