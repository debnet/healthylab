# coding: utf-8
from django.urls import path

from healthyapp import api, views


urlpatterns = [
    # TODO:
]

# API REST
router = api.router
api_urlpatterns = [
    # TODO:
] + router.urls
