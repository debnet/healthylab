# coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from healthyapp.models import Profile


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
        )}),
    )
    filter_horizontal = ('groups', 'user_permissions', )
