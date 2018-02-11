# coding: utf-8
from django.urls import path

from healthyfood import api, views


urlpatterns = ([
    # TODO:
], 'healthyfood')

# API REST
router = api.router
api_urlpatterns = ([
    # TODO:
] + router.urls, 'healthyfood')
