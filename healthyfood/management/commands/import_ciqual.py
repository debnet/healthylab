# coding: utf-8
import csv

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from healthyfood.models import FoodGroup, Food


class Command(BaseCommand):
    help = _("Import du fichier de table de composition nutritionnelle")

    def add_arguments(self, parser):
        parser.add_argument('fichier', type=str, help=_("Fichier à importer (au format CSV)"))
        parser.add_argument('--no-headers', action='store_false', dest='headers', help=_("Fichier sans entête"))

    def handle(self, file=None, headers=True, *args, **options):
        with open(file, 'r', encoding='utf8') as file:
            reader = csv.reader(file, delimiter=',')
            with transaction.atomic():
                groups = {}
                for line_number, line in enumerate(reader):
                    if not line_number and headers:
                        continue
                    group_infos = line[:6]
                    group_code, ss_group_code, ss_ss_group_code, group_name, ss_group_name, ss_ss_group_name = group_infos
                    group = groups.get((group_code, ss_group_code, ss_ss_group_code))
                    if not group:
                        group, created = FoodGroup.objects.update_or_create(
                            code=group_code,
                            defaults=dict(name=group_name, level=1))
                        if ss_group_code.replace('0', ''):
                            group, created = FoodGroup.objects.update_or_create(
                                code=ss_group_code,
                                defaults=dict(
                                    name=ss_group_name,
                                    level=2,
                                    parent=group))
                        if ss_ss_group_code.replace('0', '').strip():
                            group, created = FoodGroup.objects.update_or_create(
                                code=ss_ss_group_code,
                                defaults=dict(
                                    name=ss_ss_group_name,
                                    level=3,
                                    parent=group))
                        groups[(group_code, ss_group_code, ss_ss_group_code)] = group
                    food_infos = line[6:]
                    code, name, name_bis, *elements = food_infos
                    field_names = [f.name for f in Food._meta.fields[3:]]
                    data = dict(name=name, group=group)
                    for field_name, value in zip(field_names, elements):
                        value = value.replace('<', '').replace('-', '').replace(',', '.')\
                            .strip().replace('traces', '0.001')
                        data[field_name] = float(value or 0)
                    Food.objects.update_or_create(code=code, defaults=data)
