# coding: utf-8
from common.tests import create_api_test_class

from healthyfood.models import MODELS


RECIPES = {}

# Tests automatisées pour tous les modèles liés à une API REST
for model in MODELS:
    create_api_test_class(model, namespace='healthyfood-api', data=RECIPES.get(model, None))
