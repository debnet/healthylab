# coding: utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractUser):
    """
    Profil
    """
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE, _("Homme")),
        (FEMALE, _("Femme")),
    )
    ACTIVITIES = (
        (1, _("sédentaire")),
        (2, _("légèrement actif")),
        (3, _("actif")),
        (4, _("très actif")),
        (5, _("extrêmement actif")),
    )
    ACTIVITIES_DESCRIPTIONS = (
        (1, _("aucun exercice quotidien ou presque")),
        (2, _("vous faîtes parfois des exercices physiques 1 à 3 fois par semaine "
              "(ménage, jardinage, bricolage, marche)")),
        (3, _("vous faîtes régulièrement des exercices physiques : 3 à 5 fois par semaine "
              "(en plus d'une légère activité, vous faîtes 2 à 4 heures de sport par semaine)")),
        (4, _("vous faîtes quotidiennement du sport ou des exercices physiques soutenus")),
        (5, _("votre travail est extrêmement physique ou bien vous vous considérez comme un sportif (de haut niveau)")),
    )
    OBJECTIVES = (
        (-1, _("perdre du poids")),
        (+1, _("prendre du poids")),
    )
    PROGRESSES = (
        (0.25, _("0,25 kg / semaine")),
        (0.50, _("0,50 kg / semaine")),
        (1.00, _("1,00 kg / semaine")),
    )
    BODY_MASS = (
        (0.0, 16.5, _("dénutrition")),
        (16.5, 18.5, _("maigreur")),
        (18.5, 25.0, _("corpulence normale")),
        (25.0, 30.0, _("surpoids")),
        (30.0, 35.0, _("obésité modérée")),
        (35.0, 40.0, _("obésité sévère")),
        (40.0, 100.0, _("obésité morbide")),
    )
    BODY_FAT = (
        (0, 15, _("trop maigre")),
        (15, 20, _("normal")),
        (20, 100, _("trop de graisse")),
    )
    IDEAL_WEIGHT_FACTOR = {MALE: 4, FEMALE: 2.5}
    BODY_FAT_FACTOR = {MALE: 16.2, FEMALE: 5.4}
    BASAL_METABOLIC_RATE_FACTOR = {
        MALE: (10.0, 6.25, 5.0, 5.0),
        FEMALE: (0.0, 6.25, 5.0, -161.0)}
    BASAL_METABOLIC_RATE_BY_ACTIVITY_FACTOR = {
        1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}

    gender = models.CharField(
        max_length=1, blank=True, null=True, choices=GENDERS,
        verbose_name=_("Sexe"))
    birth_date = models.DateField(
        blank=True, null=True,
        verbose_name=_("date de naissance"))
    weight = models.FloatField(
        blank=True, null=True,
        verbose_name=_("poids actuel"))
    objective_weight = models.FloatField(
        blank=True, null=True,
        verbose_name=_("poids souhaité"))
    height = models.SmallIntegerField(
        blank=True, null=True,
        verbose_name=_("taille"))
    activity = models.PositiveSmallIntegerField(
        blank=True, null=True, choices=ACTIVITIES,
        verbose_name=_("activité"))
    objective = models.SmallIntegerField(
        blank=True, null=True, choices=OBJECTIVES,
        verbose_name=_("objectif"))
    progress = models.FloatField(
        blank=True, null=True, choices=PROGRESSES,
        verbose_name=_("progression"))

    @property
    def age(self):
        """
        Âge
        """
        if not self.birth_date:
            return None
        from datetime import date
        today, birth_date = date.today(), self.birth_date
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @property
    def ideal_weight(self):
        """
        Poids idéal selon la formule de Lorentz
        """
        if self.gender and self.height:
            factor = self.IDEAL_WEIGHT_FACTOR.get(self.gender)
            return round(self.height - 100 - ((self.height - 150) / factor), 1)
        return None

    @property
    def body_mass_index(self):
        """
        Indice de masse corporelle (IMC ou BMI)
        """
        if self.height and self.weight:
            return round(self.weight / ((self.height / 100) ** 2), 2)
        return None

    @property
    def body_mass_label(self):
        """
        Libellé de l'indice de masse corporelle
        """
        bmi = self.body_mass_index
        if not bmi:
            return None
        for mini, maxi, label in self.BODY_MASS:
            if mini <= bmi < maxi:
                return label
        return None

    @property
    def body_fat_percentage(self):
        """
        Indice de masse grasse
        """
        bmi = self.body_mass_index
        if self.gender and self.birth_date and bmi:
            factor = self.BODY_FAT_FACTOR.get(self.gender)
            return round(1.2 * bmi + 0.23 * self.age - factor, 2)
        return None

    @property
    def body_fat_label(self):
        """
        Libellé de l'indice de masse grasse
        """
        bfp = self.body_fat_percentage
        if bfp:
            factor = +10 if self.gender == self.FEMALE else 0
            for mini, maxi, label in self.BODY_FAT:
                if mini + factor <= bfp < maxi + factor:
                    return label
        return None

    @property
    def basal_metabolic_rate(self):
        """
        Métabolisme de base
        """
        if self.age and self.weight and self.height and self.gender:
            f1, f2, f3, f4 = self.BASAL_METABOLIC_RATE_FACTOR.get(self.gender)
            bmr = round(f1 * self.weight + f2 * self.height - f3 * self.age + f4, 2)
            if self.activity:
                bmr *= self.BASAL_METABOLIC_RATE_BY_ACTIVITY_FACTOR.get(self.activity)
            return round(bmr, 0)
        return None

    class Meta:
        verbose_name = _("profil")
        verbose_name_plural = _("profils")


MODELS = (Profile, )

