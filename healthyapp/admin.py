# coding: utf-8
from common.admin import create_admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from healthyapp.models import MODELS, Profile


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    """
    Administration des joueurs
    """
    fieldsets = UserAdmin.fieldsets + (
        (_("Healthy Lab"), {'fields': (
            'gender',
            'birth_date',
            'weight',
            'objective_weight',
            'height',
            'activity',
            'objective',
            'progress',
            'status',
        )}),
    )
    filter_horizontal = ('groups', 'user_permissions', )


# Création automatique des interfaces d'administration des modèles
create_admin(*MODELS)
