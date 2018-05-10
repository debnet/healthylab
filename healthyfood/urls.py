# coding: utf-8
from healthyfood import api


urlpatterns = ([
    # TODO:
], 'healthyfood')

# API REST
router = api.router
api_urlpatterns = ([
    # TODO:
] + router.urls, 'healthyfood')
