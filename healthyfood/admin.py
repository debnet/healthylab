# coding: utf-8
from common.admin import create_admin

from healthyfood.models import MODELS


# Création automatique des interfaces d'administration des modèles
create_admin(*MODELS)
