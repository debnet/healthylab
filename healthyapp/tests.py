# coding: utf-8
from common.tests import create_api_test_class

from healthyapp.models import MODELS, Profile


RECIPES = {}

# Tests automatisées pour tous les modèles liés à une API REST
for model in (Profile, ) + MODELS:
    create_api_test_class(model, namespace='healthyapp-api', data=RECIPES.get(model, None))
