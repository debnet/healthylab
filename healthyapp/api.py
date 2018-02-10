# coding: utf-8
from common.api.base import SERIALIZERS_BASE
from common.api.serializers import CommonModelSerializer
from common.api.utils import create_api, disable_relation_fields
from rest_framework import serializers

from healthyapp.models import MODELS, Profile


class ProfileSerializer(CommonModelSerializer):
    """
    Serializer spécifique des profils pour les formules de calcul
    """
    age = serializers.ReadOnlyField()
    ideal_weight = serializers.ReadOnlyField()
    body_mass_index = serializers.ReadOnlyField()
    body_mass_label = serializers.ReadOnlyField()
    body_fat_percentage = serializers.ReadOnlyField()
    body_fat_label = serializers.ReadOnlyField()
    basal_metabolic_rate = serializers.ReadOnlyField()

    class Meta:
        model = Profile


# Surcharge du serializer des profils
SERIALIZERS_BASE.update({Profile: (ProfileSerializer, )})

# Désactive les listes déroulantes sur les champs de relations
disable_relation_fields(*MODELS)

# Création des APIs REST standard pour les modèles de cette application
router, all_serializers, all_viewsets = create_api(*MODELS)
