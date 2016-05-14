"""Urls for translator API
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import TranslatorView

router = DefaultRouter()
router.register(r'translator', TranslatorView, base_name="translator")

urlpatterns = [
    url(r'^', include(router.urls)),
]
