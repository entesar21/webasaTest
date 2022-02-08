from django.urls import path
from django.conf.urls import include,url
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile',ProfileView,basename='profile')

urlpatterns=[
    url('',include(router.urls)),
    path('otp/',OTPView.as_view(),name="otp_view"),
    # path('profilee/<int:pk>/',ProfileApi.as_view()),
    path('profile_edit/<int:pk>/',ProfileEditApi.as_view()),
]
