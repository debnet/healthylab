# coding: utf-8
from healthyapp import api


urlpatterns = ([
    # TODO:
], 'healthyapp')

# API REST
router = api.router
api_urlpatterns = ([
    # TODO:
] + router.urls, 'healthyapp')
