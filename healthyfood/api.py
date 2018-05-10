# coding: utf-8
from common.api.base import SERIALIZERS_BASE
from common.api.serializers import CommonModelSerializer
from common.api.utils import create_api, disable_relation_fields
from rest_framework import serializers

from healthyfood.models import MODELS, Meal, MealPortion, Order, OrderItem


class MealSerializer(CommonModelSerializer):
    """
    Serializer spécifique pour les portions
    """
    low_energy = serializers.ReadOnlyField()
    low_protein = serializers.ReadOnlyField()
    low_carb = serializers.ReadOnlyField()
    low_lipid = serializers.ReadOnlyField()
    base_energy = serializers.ReadOnlyField()
    base_protein = serializers.ReadOnlyField()
    base_carb = serializers.ReadOnlyField()
    base_lipid = serializers.ReadOnlyField()
    high_energy = serializers.ReadOnlyField()
    high_protein = serializers.ReadOnlyField()
    high_carb = serializers.ReadOnlyField()
    high_lipid = serializers.ReadOnlyField()

    class Meta:
        model = Meal


class MealPortionSerializer(CommonModelSerializer):
    """
    Serializer spécifique pour les portions
    """
    energy = serializers.ReadOnlyField()
    protein = serializers.ReadOnlyField()
    carb = serializers.ReadOnlyField()
    lipid = serializers.ReadOnlyField()

    class Meta:
        model = MealPortion


class OrderSerializer(CommonModelSerializer):
    """
    Sérializer spécifique pour les commandes
    """
    price = serializers.ReadOnlyField()

    class Meta:
        model = Order


class OrderItemSerializer(CommonModelSerializer):
    """
    Sérializer spécifique pour les éléments de commande
    """
    price = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem


# Surcharge du serializer des profils
SERIALIZERS_BASE.update({
    Meal: (MealSerializer, ),
    MealPortion: (MealPortionSerializer, ),
    Order: (OrderSerializer, ),
    OrderItem: (OrderItemSerializer, ),
})

# Désactive les listes déroulantes sur les champs de relations
disable_relation_fields(*MODELS)

# Création des APIs REST standard pour les modèles de cette application
router, all_serializers, all_viewsets = create_api(*MODELS)
