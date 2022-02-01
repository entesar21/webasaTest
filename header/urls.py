from django.template.defaulttags import url
from django.urls import path
from django.conf.urls import include,url
# from rest_framework import routers

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('menu',MenuViewSet)
router.register('logo',LogoViewSet)


urlpatterns = [
    url('',include(router.urls)),
]
